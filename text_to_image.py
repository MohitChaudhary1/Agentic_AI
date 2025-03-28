from smolagents import CodeAgent, HfApiModel, tool, Tool
from huggingface_hub import list_models, InferenceClient
from dotenv import load_dotenv

load_dotenv()

@tool
def model_download_tool(task: str) -> str:
    """Finds the most downloaded Hugging Face model for a specific task type.
    
    Args:
        task (str): The type of model to search for (e.g., 'text-generation', 
                   'text-to-image'). See Hugging Face tasks for valid options.
    
    Returns:
        str: Model ID of the most downloaded model
    """
    return next(iter(list_models(filter=task, sort="downloads", direction=-1))).id

class TextToImageTool(Tool):
    description = "Generates images from text prompts using Hugging Face models"
    name = "image_generator"
    inputs = {
        "prompt": {"type": "string", "description": "Text description of the image"},
        "model": {"type": "string", "description": "Optional model ID", "nullable": True}
    }
    output_type = "image"
    current_model = "stabilityai/stable-diffusion-xl-base-1.0"

    def __init__(self):
        super().__init__()
        self.client = InferenceClient(self.current_model)

    def forward(self, prompt: str, model: str = None):
        if model:
            self.client = InferenceClient(model)
        image = self.client.text_to_image(prompt)
        image.save("output.png")
        return f"Generated image using {model or self.current_model}"

agent = CodeAgent(
    tools=[TextToImageTool(), model_download_tool],
    model=HfApiModel()
)

result = agent.run("Generate an image of a robot cat painting a landscape. Get the latest model from text-to-image from the Hugging Face Hub")
print(result)