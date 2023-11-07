import json
import os
import random
import folder_paths
import comfy.sd
import comfy.utils
from consistencydecoder import ConsistencyDecoder, save_image, load_image
import numpy as np
import torch
from PIL import Image 



class ConsistencyDecoderWrapper:
    def __init__(self, decoder):
        self.decoder = decoder
    def decode(self, x):
        return self.decoder(x)

class ConsistencyDecoderLoader:
    RETURN_TYPES = ("VAE",)
    FUNCTION = "load_consistency_decoder"

    CATEGORY = "ConsistencyDecoderNode"

    def load_consistency_decoder(self):
        consistencyDecoder = ConsistencyDecoder(device="cuda:0")
        vae = ConsistencyDecoderWrapper(consistencyDecoder)
        return (vae,)

class ConsistencyDecode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "samples": ("LATENT", ), "vae": ("VAE", )}}
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "decode"

    CATEGORY = "ConsistencyDecoderNode"

    def decode(self, vae, samples):
        image = vae.decode(samples["samples"].to("cuda:0"))
        image = image[0].cpu().numpy()
        image = (image + 1.0) * 127.5
        image = image.clip(0, 255).astype(np.uint8)
        image = Image.fromarray(image.transpose(1, 2, 0))
        image = image.convert("RGB")
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        return (image, )

NODE_CLASS_MAPPINGS = {
    "ConsistencyDecoderLoader": ConsistencyDecoderLoader,
    "ConsistencyDecode": ConsistencyDecode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ConsistencyDecoderLoader": "ConsistencyDecoderLoader",
    "ConsistencyDecode": "ConsistencyDecode",
}