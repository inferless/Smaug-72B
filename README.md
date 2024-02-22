# Tutorial - Deploy Smaug-72B
- Smaug-72B - which is a current topper of the Hugging Face LLM leaderboard and it’s the first model with an average score of 80.
- Check out [this tutorial](https://tutorials.inferless.com/deploy-openllm-leaderboard-topper-smaug-72b-using-inferless) which will guide you through the process of deploying a Smaug-72B model using Inferless.

## TL;DR - Deploy Smaug-72B using Inferless:
- Deployment of Deploy Smaug-72B model using [vLLM](https://github.com/vllm-project/vllm).

- By using the vLLM, you can expect an average latency of 8.01 sec, generating an average of 29.94 tokens/sec where each token took 33.39 ms and an average cold start time of 26.65 sec using an A100 GPU(80GB).
- Dependencies defined in inferless-runtime-config.yaml.
- GitHub/GitLab template creation with app.py and config.yaml.
- Model class in app.py with initialize, infer, and finalize functions.
- Custom runtime creation with necessary system and Python packages.
- Model import via GitHub with input/output parameters in JSON.
- Recommended GPU: NVIDIA A100 for optimal performance.
- Custom runtime selection in advanced configuration.
- Final review and deployment on the Inferless platform.

---
## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the app.py according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

---
## Quick Start
Here is a quick start to help you get up and running with this template on Inferless.

### Download the config-vllm and Create a runtime 
Get started by downloading the config.yaml file and go to Inferless dashboard and create a custom runtime 

Quickly add this as a Custom runtime

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.


### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the Add Model button.

Select the PyTorch as framework and choose **Repo(custom code)** as your model source and use the forked repo URL as the **Model URL**.

After the create model step, while setting the configuration for the model make sure to select the appropriate runtime.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/github-custom-code) for more information on model import.

The following is a sample Input and Output JSON for this model which you can use while importing this model on Inferless.

### Input
```json
{
  "inputs": [
    {
      "data": [
        "What is quantization?"
      ],
      "name": "prompt",
      "shape": [
        1
      ],
      "datatype": "BYTES"
    }
  ]
}
```

### Output
```json
{
  "outputs": [
    {
      "data": [
        "data"
      ],
      "name": "generated_result",
      "shape": [
        1
      ],
      "datatype": "BYTES"
    }
  ]
}
```

---
## Curl Command
Following is an example of the curl command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.
```bash
curl --location '<your_inference_url>' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer <your_api_key>' \
          --data '{
                  "inputs": [
                    {
                      "data": [
                        "What is quantization?"
                      ],
                      "name": "prompt",
                      "shape": [
                        1
                      ],
                      "datatype": "BYTES"
                    }
                  ]
                }
            '
```


---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting `self.pipe = None`.


For more information refer to the [Inferless docs](https://docs.inferless.com/).
