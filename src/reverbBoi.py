import warnings
from ddsp.training import (data, decoders, encoders, models, preprocessing, train_util)

warnings.filterwarnings("ignore")


sample_rate = 16000

# Get a single example from NSynth.
# Takes a few seconds to load from GCS.

ddsp_prepare_tfrecord \
  --input_audio_filepatterns=/path/to/wavs/*wav \
  --output_tfrecord_path=/path/to/dataset_name.tfrecord \
  --num_shards=10 \
  --alsologtostderr
