# Installing JAX on the Jetson Nano

I followed [these instructions](https://forums.developer.nvidia.com/t/jax-on-jetson-nano/182593/9)

with minor changes: 

1. I used a 500 GB SSD
2. I set the swap size to 16GB, not 10GB
3. I had also to do `sudo apt install python3.9-distutils` before I could install into my virtual environment with pip.