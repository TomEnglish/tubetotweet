import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "\nYou will be given an image of a process diagram. Your task is to create a detailed summary of all the workflows, capturing the proportion and absolute number of persons moved in each direction from each station.\n\nHere is the process diagram image:\n<process_diagram>"
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": "<base64_encoded_image>"
                    }
                },
                {
                    "type": "text",
                    "text": "</process_diagram>\n\nAnalyze the image carefully, paying attention to all stations, connections, and any numerical information provided.\n\nStructure your summary as follows:\n\n1. Start with a brief overview of the entire process, mentioning the total number of stations and major workflows.\n\n2. For each station in the diagram:\n   a. Identify the station name and list any total associated with the station\n   b. List all ingoing and outgoing connections from this station\n   c. For each connection, provide:\n      - The destination station\n      - The proportion of people moving in this direction (as a percentage)\n      - The absolute number of people moving in this direction\n\n\nUse the following format for your detailed analysis:\n\n<analysis>\n[Overview of the entire process]\n\nStation: [Station Name/Number]\n- To [Destination 1]: [Percentage]% ([Absolute Number] people)\n- To [Destination 2]: [Percentage]% ([Absolute Number] people)\n[Continue for all connections from this station]\n\n[Repeat for all stations]\n\nFinal Summary:\n[Provide insights as described above]\n</analysis>\n\nEnsure that your percentages add up to 100% for each station's outgoing connections, and that the absolute numbers are consistent with the proportions given.\n\nIf any information is unclear or not provided in the image, state this clearly in your analysis.\n\nRemember to be thorough and accurate in your description of the workflow, capturing all the details present in the diagram."
                }
            ]
        }
    ]
)
print(message.content)