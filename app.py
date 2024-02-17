import os
from vllm import SamplingParams
from vllm import LLM
from huggingface_hub import snapshot_download


class InferlessPythonModel:
    def initialize(self):
        self.template = """SYSTEM: You are a helpful assistant.
        USER: {}
        ASSISTANT: """
        snapshot_download(
            "TheBloke/CodeLlama-7B-Python-AWQ",
            local_dir="/model",
            token="<<your_token>>",
        )
        self.llm = LLM(
          model="/model",
          quantization="awq",
          dtype="float16")
    
    def infer(self, inputs):
        print("inputs[prompt] -->", inputs["prompt"], flush=True)
        prompts = inputs["prompt"]
        print("Prompts -->", prompts, flush=True)
        sampling_params = SamplingParams(
            temperature=1.0,
            top_p=1,
            max_tokens=512
        )
        result = self.llm.generate(prompts, sampling_params)
        result_output = [output.outputs[0].text for output in result]

        return {"result": result_output[0]}

    def finalize(self, args):
        pass
