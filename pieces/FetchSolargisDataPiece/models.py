from pydantic import BaseModel

class InputModel(BaseModel):
    """
    Fetch Solargis Data Piece Input Model
    """
    data_input_path: str = Field(
        title="Path to input data files",
        default='/home/shared_storage/input_data/InputFile.doc',
        description="The path to input meteo data files"
    )    

    data_output_path: str = Field(
        title="Path to output data file",
        default='/home/shared_storage/data/File.csvc',
        description="The path to output meteo data file"
    )
    
class OutputModel(BaseModel):
    """
    Fetch Solargis Data Piece Output Model
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )

    file_path: str = Field(
        description="The path & file name to the output CSV file"
    )