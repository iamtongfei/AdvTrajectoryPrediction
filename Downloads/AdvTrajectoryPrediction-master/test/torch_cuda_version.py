import  torch

print(torch.cuda.is_available())

# If the output of this command is True, 
# then Torch has been compiled with CUDA support, and you should be able to use it with the GPU. If the output is False, Torch does not have CUDA support, and you will need to either install the correct binary with the correct CUDA version or recompile it with your current CUDA version.


print("Torch version:",torch.__version__) #Torch version: 1.10.2

print("Is CUDA enabled?",torch.cuda.is_available())