from pydantic import BaseModel, Field

class InputModel(BaseModel):
    data_path: str = Field(
        title="Path to data file",
        default='/home/shared_storage/data/DataForPrediction.csv',
        description="The path to data file for prediction"
    ) 
    model_path: str = Field(
        title="Path to model file",
        default='/home/shared_storage/data/model.pkl',
        description="The path to prediction model file"
    ) 
    metrics_out: str = Field(
        title="Path to metrics output file",
        default='/home/shared_storage/data/metrics.json',
        description="The path to metrics output file"
    ) 
    plot_out: str = Field(
        title="Path to graphical prediction output file",
        default='/home/shared_storage/data/comparison.png',
        description="The path to graphical prediction output file"
    ) 

class OutputModel(BaseModel):
    message: str= Field(
        default="",
        description="Output message to log"
    )
    metrics_file: str= Field(
        default="",
        description="The path to the metrics json file"
    )
    plot_file: str= Field(
        default="",
        description="The path to the graphical prediction output file"
    )
    mae: float
    r2: float