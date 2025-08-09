from textsummarize.config.configuration import ConfigurationManager
from textsummarize.components.data_transformation import DataTransformation
from textsummarize.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()