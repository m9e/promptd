from pydantic import BaseModel, Field
from typing import List, Callable

class BaseTool(BaseModel):
    name: str = Field(..., description="The short name of the tool.")
    description: str = Field(..., description="The description of the tool.")
    call: Callable = Field(..., description="The function to be used for the tool.")

class BasePrompt(BaseModel):
    name: str = Field(..., description="The short name of the prompt.")
    task: str = Field(..., description="The task to be accomplished.")
    context: str = Field(..., description="The context for the task.")
    prompt: str = Field(..., default="{prompt}", description="The prompt to be used for the task.")

    tools: List[BaseTool] = Field(..., description="The tools to be used for the task.")