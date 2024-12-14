#from whisper_live.client import TranscriptionClient
from client_custom import TranscriptionClient

client = TranscriptionClient(
  "dc-max.local", #"localhost",
  9090,
  lang="en",
  translate=False,
  model="medium.en", #model="tiny.en",
  use_vad=True,
  save_output_recording=True,
)
client()