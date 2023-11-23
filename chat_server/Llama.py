from transformers import AutoTokenizer
import transformers
import torch


class Llama:
    model = "meta-llama/Llama-2-7b-chat-hf"
    tokenizer = None
    pipeline = None
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.model)
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model,
            torch_dtype=torch.float16,
            device_map="auto",
        )

    def text_generation(self, input_text):
        sequences = self.pipeline(
            input_text,
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=self.tokenizer.eos_token_id,
            max_length=200,
        )
        return sequences[0]['generated_text']

class LLMMockup:
    name = "Mockup"
    def text_generation(self, input_text):
        return f"{self.name}-text_generation :{input_text}"
