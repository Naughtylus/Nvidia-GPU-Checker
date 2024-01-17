
# Nvidia GPU Checker for Ubuntu

To check if your Nvidia GPU CUDA cores is being utilized for Machine Learning Development.



## Requirements

- [PyTorch](https://pytorch.org/)


## Installation

`git clone https://github.com/Naughtylus/Nvidia-GPU-Checker.git`

Run the functions required on the Python file provided.

## Usage

| Function                      | Action                                         |
| ----------------------------- | ---------------------------------------------- |
| `isInstalled()`|Checks if Nvidia Driver is installed|
| `basicInformation()`|Provides current index of GPU, numbers of GPU available, and GPU model.|
| `advanceInformation()`|Provides memory information about current GPU memory information)|
| `watch_nvidia_smi()`| Runs the watch_nvidia_smi command with a refresh of x seconds (Pass a number) |
