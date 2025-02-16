import json
from src.consts import input_data_file, output_data_file, system_message

def prepare_training_dataset(input_file, output_file, system_message):
    try:
        # Create the base conversation template
        conversation_template = {
            "schemaVersion": "bedrock-conversation-2024",
            "system": [{"text": system_message}],
            "messages": []
        }
        
        # Process input file and write output
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Read input file line by line
            for line in infile:
                if line.strip():  # Skip empty lines
                    # Parse the input JSON line
                    input_data = json.loads(line)
                    
                    # Create a new conversation for each line
                    conversation = conversation_template.copy()
                    
                    # Add user message
                    user_message = {
                        "role": "user",
                        "content": [{"text": input_data["prompt"]}]
                    }
                    
                    # Add assistant message
                    assistant_message = {
                        "role": "assistant",
                        "content": [{"text": input_data["completion"]}]
                    }
                    
                    # Add messages to conversation
                    conversation["messages"] = [user_message, assistant_message]
                    
                    # Write the conversation to output file
                    outfile.write(json.dumps(conversation) + '\n')
                
        print(f"Successfully converted {input_file} to Bedrock format and saved to {output_file}")
        return True
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return False

prepare_training_dataset(
    input_file=input_data_file,
    output_file=output_data_file,
    system_message=system_message
)