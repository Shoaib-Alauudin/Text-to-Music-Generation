# Text to Music Generator

This Streamlit web application allows you to generate music from text descriptions using the MusicGen Small model from Facebook's Audiocraft library.

## Overview

This application provides an intuitive interface for users to input text descriptions, specifying the desired duration of the generated music. The provided text is used to generate corresponding music, which can be played back and downloaded. The application utilizes Facebook's Audiocraft library and the MusicGen Small model for music generation.

## Features

- **Text Input:** Users can enter text descriptions to generate music from.

- **Music Generation:** Upon clicking the "Generate" button, the application generates music based on the provided text using the MusicGen Small model.

- **Playback and Download:** The generated music can be played back within the application, and users can download the generated music files.

## Prerequisites

- Python 3.6+
- Streamlit
- Audiocraft library (`audiocraft` package)
- Torchaudio
- Transformers library (`transformers` package)

You can install the required dependencies using the following command:
```bash
pip install streamlit audiocraft torchaudio transformers
```
<br>

**Note**: The application uses the MusicGen Small model from Facebook's Audiocraft library. Instead of cloning the model repository from GitHub, it fetches the model directly from the Hugging Face model hub during runtime.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/Shoaib-Alauudin/Text-to-Music-Generation.git

    cd text-to-music-generator
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4.  Input your text description and select the desired time duration. Click the "Generate" button to create and listen to the generated music.

5.  You can play the generated music within the application. To download the generated music file, use the provided download link.

## Acknowledgments
*   The MusicGen Small model is provided by Facebook's Audiocraft library.

*   This project showcases text-to-music capabilities using Hugging Face's Transformers library and Facebook's Audiocraft.