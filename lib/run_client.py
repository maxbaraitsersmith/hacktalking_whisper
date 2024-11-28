from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
  "dc-max.local",
  9090,
  lang="en",
  translate=False,
  model="tiny.en",
  use_vad=True,
  save_output_recording=True,
  output_recording_filename="./output/output.wav",
)
client()