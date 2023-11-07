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


class ConsistencyDecode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "samples": ("LATENT", )}}
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "decode"

    CATEGORY = "ConsistencyDecoderNode"

    def decode(self, samples):
        consistencyDecoder = ConsistencyDecoder(device="cuda:0")
        images = consistencyDecoder(samples["samples"].to("cuda:0")).cpu().numpy()
        # create result torch tensor
        result = torch.zeros(images.shape[0],images.shape[2],images.shape[3],images.shape[1]).cpu()
        # print('value',images.shape[0],images.shape[2],images.shape[3],images.shape[1])
        # print('image.shape',result.shape)
        # print('result.shape',result.shape)
        # loop images
        for i in range(len(images)):
            image = (images[i] + 1.0) * 127.5
            image = image.clip(0, 255).astype(np.uint8)
            image = Image.fromarray(image.transpose(1, 2, 0))
            image = image.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]

            # put image in result
            result[i] = image
        return (result, )

NODE_CLASS_MAPPINGS = {
    "ConsistencyDecode": ConsistencyDecode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ConsistencyDecode": "ConsistencyDecode",
}