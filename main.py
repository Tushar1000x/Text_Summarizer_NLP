from src.textsummarize.pipeline.stage01_dataIngestion import DataIngestionTrainingPipeline
from src.textsummarize.pipeline.stage02_dataValidation import DataValidationTrainingPipeline
from src.textsummarize.pipeline.stage03_dataTransformation import DataTransformationTrainingPipeline
from src.textsummarize.pipeline.stage04_modelTrainer import ModelTrainerTrainingPipeline
from src.textsummarize.pipeline.stage05_modelEvaluation import ModelEvaluationTrainingPipeline
from src.textsummarize.logging import logger




STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion =  DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation =  DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transforamtion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_Transformation =  DataTransformationTrainingPipeline()
   data_Transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data ModelTrainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_modelTrainer =  ModelTrainerTrainingPipeline()
   data_modelTrainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data ModelEval stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_modelEval =  ModelEvaluationTrainingPipeline()
   data_modelEval.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e