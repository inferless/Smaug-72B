from vllm import LLM, SamplingParams

class InferlessPythonModel:
    def initialize(self):

        self.sampling_params = SamplingParams(temperature=0.7, top_p=0.95,max_tokens=256)
        self.llm = LLM(model="LoneStriker/Smaug-72B-v0.1-GPTQ", quantization="gptq", dtype="float16",max_model_len=2048,gpu_memory_utilization=0.9)

    def infer(self, inputs):
        prompts = inputs["prompt"]
        result = self.llm.generate(prompts, self.sampling_params)
        result_output = [output.outputs[0].text for output in result]

        return {'generated_result': result_output[0]}

    def finalize(self):
        pass
