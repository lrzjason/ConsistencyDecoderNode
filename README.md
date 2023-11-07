# Consistency Decoder For Comfyui

This project is a comfyui node adaption of Consistency Decoder (https://github.com/openai/consistencydecoder).

- 20231107
Support multiple images but it would exceed 24GB vram usage. 
Please don't use with batch size more than 2.

## Installation

```bash
pip install git+https://github.com/openai/consistencydecoder.git
```
- goto ComfyUI\custom_nodes
```bash
git clone https://github.com/lrzjason/ConsistencyDecoderNode
```

Please download the model from following link 
```bash
https://openaipublic.azureedge.net/diff-vae/c9cebd3132dd9c42936d803e33424145a748843c8f716c0814838bdc8a2fe7cb/decoder.pt
```
place the model to 
```bash
C:\\Users\\[user]/.cache/clip
```

# Hardware Requirement
- 24GB vram at peak

# Example
It only works with SD1.5 latent mapping
![alt text](https://github.com/lrzjason/ConsistencyDecoderNode/blob/main/assets/example.png?raw=true)
