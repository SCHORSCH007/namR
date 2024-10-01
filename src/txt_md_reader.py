import re
import os

def txt_md_strategy(file_path, wrapper: str="only return an adequate filename to the following text-file", description:str=None):
    text = read_file(file_path=file_path)
    
    first_words = ""
    description_str = ""
    
    if description:
        description_str = f"\n description what the file is: ```{description}```"
    if text:
        first_words = ' '.join(text)
    
    string_request = f"{wrapper} {description_str} \n first words: ```{first_words}``` \n only return an adequate filename"
    
    return string_request

    
def read_file (file_path: str, count: int=100):
    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.", end="")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Use regex to split content into words, ignoring punctuation
            words = re.findall(r'\b\w+\b', content)

            return words[:count]
    except Exception as e:
        raise IOError(f"An error occurred while reading the file: {e}")
