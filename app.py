from audiocraft.models import MusicGen
import streamlit as st
import os
import torch
import torchaudio
import numpy as np
import base64
import uuid

@st.cache_resource
def load_model():
     model = MusicGen.get_pretrained("facebook/musicgen-small")
     return model

# It will generate the music and return in tensor format
def generate_music_tensor(description:str, duration:int):

    print("Description: ", description)
    print("Duration: ", duration)
    model = load_model()
    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=duration
    )

    results = model.generate(
        descriptions=[description], 
        progress=True, 
        return_tokens=True)
    
    return results[0]

def save_music(samples: torch.Tensor):
    sample_rate = 32000
    save_path = "music_output/"

    assert samples.dim() == 2 or samples.dim() == 3
    samples = samples.detach().cpu()

    if samples.dim() == 2:
        samples = samples[None, ...]

    for idx, music_sample in enumerate(samples):
        unique_id = uuid.uuid4().hex  # Generate a unique identifier
        music_path = os.path.join(save_path, "music_{}_{}.wav".format(unique_id, idx))
        torchaudio.save(music_path, music_sample, sample_rate)

def get_binary_music_file_download(bin_file, file_label='Music file'):
    with open(bin_file, 'rb') as f:
        data = f.read()

    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" \
        download="{os.path.basename(bin_file)}"> Download {file_label}</a>' 

    return href  

st.set_page_config(
     page_icon=":musical_note:",
     page_title="Music Generator"
)

def main():
    st.title("Text to Music Generator")
    
    with st.expander("See explanation"):
        st.write("Music Generator app built using Meta's Audiocraft library. We are using Music Gen Small model.")

    text_area = st.text_area("Enter your text to generate music")
    time_slider = st.slider("Select time duration (seconds):", 0, 30, 10)

    if text_area and time_slider:
        st.json(
            {
                "Entered Text Description": text_area,
                "Selected Time Duration (seconds)": time_slider
            }
        )

        st.subheader("Generated Music")
        music_tensor = generate_music_tensor(text_area, time_slider)
        print("Music Tensor:", music_tensor)
        save_music_file = save_music(music_tensor)

        music_files = os.listdir("music_output/")  # List all saved music files
        music_paths = [os.path.join("music_output", file) for file in music_files]

        for music_path in music_paths:
            music_file = open(music_path, 'rb')
            music_bytes = music_file.read()

            st.audio(music_bytes, format="audio/wav")
            st.markdown(get_binary_music_file_download(music_path, "Music"), unsafe_allow_html=True)
                     
if __name__ == "__main__":
    main()