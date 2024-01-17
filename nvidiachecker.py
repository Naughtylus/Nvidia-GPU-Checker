# import PyTorch
import torch
import subprocess

# Check if Nvidia Driver installed
def isInstalled():
  cudaAvailable = torch.cuda.is_available()

  if cudaAvailable == True:
    print("Nvidia Driver installed")
  else:
    print("Nvidia Driver not installed")

# Check for basic information regarding cuda device
def basicInformation():
  print("Index of Current Device: " + str(torch.cuda.current_device()))

  # get number of GPUs available
  print("Number of GPUs available: " + str(torch.cuda.device_count()))


  # get the name of the device
  print("GPU Name: " + str(torch.cuda.get_device_name(0)))

def advanceInformation():
  # Sets to GPU, if not available then CPU
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  print('Using device:', device)


  #Additional Info when using cuda
  if device.type == 'cuda':
      print(torch.cuda.get_device_name(0))
      print('Memory Usage:')
      print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
      print('Cached:   ', round(torch.cuda.memory_cached(0)/1024**3,1), 'GB')

def watch_nvidia_smi():
  try:
    print("CTRL + C to stop")
    # Updates every 2 seconds
    # watch -n 2 nvidia-smi
    subprocess.run(['watch', '-n', '2', 'nvidia-smi'], check=True)
  except subprocess.CalledProcessError as e:
    print(f"Error occurred: {str(e)}")

