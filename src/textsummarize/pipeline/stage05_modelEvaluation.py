from textsummarize.config.configuration import ConfigurationManager
from textsummarize.components.model_eval import ModelEvaluation
from textsummarize.logging import logger



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()
        
if __name__ == "__main__":
    print('Calling main')
    pipeline = ModelEvaluationTrainingPipeline()
    pipeline.main()