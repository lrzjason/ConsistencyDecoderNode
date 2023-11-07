# Consistency Decoder For Comfyui

This project is an node adaption of Consistency Decoder(https://github.com/openai/consistencydecoder).

## Installation

- pip install git+https://github.com/openai/consistencydecoder.git
- goto ComfyUI\custom_nodes
```bash
git clone https://github.com/lrzjason/ConsistencyDecoderNode
```

Please download the following link and place the model to 
```bash
C:\\Users\\[user]/.cache/clip
```
if neccessary
https://openaipublic.azureedge.net/diff-vae/c9cebd3132dd9c42936d803e33424145a748843c8f716c0814838bdc8a2fe7cb/decoder.pt

# Hardware Requirement
- 24GB vram at peak

# Example
It only works with SD1.5 latent mapping
![alt text](https://github.com/lrzjason/ConsistencyDecoderNode/blob/main/assets/example.png?raw=true)
