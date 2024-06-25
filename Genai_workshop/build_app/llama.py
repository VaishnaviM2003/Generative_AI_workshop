from clarifai.client.workflow import Workflow

# Initialize the workflow_url and PAT
workflow_url = "https://clarifai.com/ptu6ctw30tqs/12345/workflows/workflow-a37b46"
pat = "99186101e6f14102855b5a44dfb4487d"
text_classification_workflow = Workflow(url=workflow_url, pat=pat)

def get_response(prompt):
    try:
        result = text_classification_workflow.predict_by_bytes(prompt.encode(), input_type="text")
        return result.results[0].outputs[0].data
    except Exception as e:
        print(f"Error in get_response: {e}")
        return "Error occurred during prediction"
