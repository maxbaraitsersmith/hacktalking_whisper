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
`$bash scripts/setup.sh`
`$pip install whisper-live`