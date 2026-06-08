from pydantic.v1 import BaseModel, Field


class SolModuleConfiguration(BaseModel):
    base_url: str = Field(..., description="Base URL of the Sekoia instance")
    api_key: str = Field(secret=True, description="API Key")
