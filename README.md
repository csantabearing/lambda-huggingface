# Triton Server

  docker run --gpus=1 --env-file .envs3 --rm --net=host nvcr.io/nvidia/tritonserver:22.06-py3 tritonserver --model-repository=s3://triton-repository/models/
