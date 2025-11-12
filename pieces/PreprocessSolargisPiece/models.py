from pydantic import BaseModel, Field

class InputModel(BaseModel):
    input_path: str = Field(
        title="Path to raw data file",
        default='/home/shared_storage/data/raw_solargis.csv',
        description="The path to the input Solargis raw data file "
    )    

    output_path: str = Field(
        title="Path to output data file",
        default='/home/shared_storage/data/processed_solargis.csv',
        description="The path to the output processed Solargis data file"
    )

class OutputModel(BaseModel):
    message: str = Field(
        default="",
        description="Output message to log"
    )
    processed_rows: int
    output_file: str = Field(
        description="The path to the output CSV file"
    )