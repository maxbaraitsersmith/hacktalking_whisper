#from whisper_live.client import TranscriptionClient
from client_custom import TranscriptionClient

client = TranscriptionClient(
  "dc-max.local",
  9090,
  lang="en",
  translate=False,
  model="tiny.en",
  use_vad=True,
  save_output_recording=True,
)
client()