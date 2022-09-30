import random
import string
from datetime import datetime, timezone
from random import choice, uniform
from typing import Hashable
from uuid import uuid4

from pydantic import BaseSettings

from mlserver_inference_pipeline.extractors.base import AbstractFeatureExtractor
from mlserver_inference_pipeline.models import FeatureRecord, FeatureSet


class RandomFeatureExtractorConfig(BaseSettings):

    seed: Hashable = datetime.now(timezone.utc)
    n_features: int
    length: int = 1

    class Config:
        env_prefix = "EXTRACTOR_RANDOM_"


class RandomFeatureExtractor(AbstractFeatureExtractor):
    def __init__(self) -> None:
        self.config = RandomFeatureExtractorConfig()
        random.seed(self.config.seed)

    def extract(self) -> FeatureSet:
        def randomword(length):
            letters = string.ascii_lowercase
            return "".join(choice(letters) for i in range(length))

        records = [
            FeatureRecord(
                ref=uuid4(),
                features=[uniform(0, 1) for _ in range(self.config.n_features)],
            )
            for _ in range(self.config.length)
        ]
        columns = [randomword(10) for _ in range(self.config.n_features)]
        return FeatureSet(records=records, columns=columns)
