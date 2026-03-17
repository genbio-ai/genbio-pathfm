import torch
from model import GenBio_PathFM_Inference
import numpy as np
from PIL import Image

# 1. Initialize the encoder
weights_path = "model.pth"
encoder = GenBio_PathFM_Inference(weights_path, device="cuda")  # Use "cpu" if CUDA is unavailable

# 2. Generate a random PIL Image (224x224 RGB)
random_array = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
dummy_img = Image.fromarray(random_array)

# 3. Preprocess the image
img_tensor = encoder.transform(dummy_img).unsqueeze(0).to(encoder.device)

# 4a. Run inference — CLS token only
with torch.no_grad():
    features_cls = encoder(img_tensor)

print(f"CLS Feature shape: {features_cls.shape}")
# Expected: [1, 4608]  (1 x embed_dim*3)

# 4b. Run inference — CLS + patch tokens
with torch.no_grad():
    features_cls, features_patches = encoder.forward_with_patches(img_tensor)

print(f"CLS Feature shape:   {features_cls.shape}")
# Expected: [1, 4608]         (1 x embed_dim*3)
print(f"Patch Feature shape: {features_patches.shape}")
# Expected: [1, 196, 4608]    (1 x num_patches x embed_dim*3)