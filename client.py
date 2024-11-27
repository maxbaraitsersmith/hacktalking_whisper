from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
  "localhost",,
  9090,
  lang="en",
  translate=False,
  model="tiny.en",
  use_vad=True,
  save_output_recording=True,
  output_recording_filename="./output.wav",
)
client()