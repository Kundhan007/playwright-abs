from bs4 import BeautifulSoup
import requests
import json

def extract_form_elements(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    forms = []

    for form in soup.find_all('form'):
        form_info = {
            'action': form.get('action'),
            'method': form.get('method', 'GET').upper(),
            'inputs': [],
            'buttons': []
        }

        # Extract inputs
        for input_tag in form.find_all('input'):
            form_info['inputs'].append({
                'type': input_tag.get('type', 'text'),
                'name': input_tag.get('name'),
                'placeholder': input_tag.get('placeholder')
            })

        # Extract textareas
        for textarea in form.find_all('textarea'):
            form_info['inputs'].append({
                'type': 'textarea',
                'name': textarea.get('name'),
                'placeholder': textarea.get('placeholder')
            })

        # Extract selects (dropdowns)
        for select in form.find_all('select'):
            options = [option.get('value') for option in select.find_all('option')]
            form_info['inputs'].append({
                'type': 'select',
                'name': select.get('name'),
                'options': options
            })

        # Extract buttons
        for button in form.find_all('button'):
            form_info['buttons'].append({
                'type': button.get('type', 'submit'),
                'name': button.get('name'),
                'text': button.text.strip()
            })

        forms.append(form_info)

    return forms

# ----- this is usage for local file -----
def parse_forms(source, from_url=False):
    if from_url:
        response = requests.get(source)
        html_content = response.text
    else:
        with open(source, 'r', encoding='utf-8') as file:
            html_content = file.read()

    forms_data = extract_form_elements(html_content)
    return forms_data

def parse_forms_static(source, output_file, from_url=False):
    forms_data = parse_forms(source, from_url)
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(forms_data, json_file, indent=4)
    return forms_data
