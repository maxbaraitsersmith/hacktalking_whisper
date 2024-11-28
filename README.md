# sharedunderstandings

**Build instructions**

install apt dependencies
`$sudo apt install unzip`

install pyenv
`$curl https://pyenv.run | bash`
`$exec "$SHELL" #restart shell`

install build dependencies (https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
	`$sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev`

`$pyenv install 3.11.2`
`$pyenv global 3.11.2`

setup venv
`$python -m venv venv`
`source venv/bin/activate`

get whisper-live
`$wget https://github.com/collabora/WhisperLive/archive/refs/tags/v0.5.1.zip`
`$unzip v0.5.1.zip`

install whisper-live
`$sudo bash WhisperLive-0.5.1/scripts/setup.sh`
`$pip install --force-reinstall -v "whisper-live==0.5.1"`
`$pip install --force-reinstall -v "numpy<2>"`

run the server and the client
`$sh server.sh`
`$python client.py`

installing cuDNN (for nvidia GPUs)

WhisperLive-0.5.1 uses ctranslate2 v4.5.0, which uses cuDNN 9. So, we must manually install the cudnn toolkit (V12) and then cudnn (v9)

Install nvidia drivers:
    `$sudo ubuntu-drivers install`
    `$nvidia-smi #check drivers work`

Installed cudnn drivers using apt:
    `$sudo apt install nvidia-cuda-toolkit`
    `$nvcc --version #verify cuda install`

Download cuDNN installer from nvidia website, and followed instructions for installing cuDNN 12
    instructions at https://developer.nvidia.com/cudnn-downloads
	`$sudo apt-get -y install cudnn`
