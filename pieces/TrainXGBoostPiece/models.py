from pydantic import BaseModel

class InputModel(BaseModel):
    data_path: str
    model_out: str
    log_out: str

class OutputModel(BaseModel):
    message: str
    model_file: str
    training_log: str
