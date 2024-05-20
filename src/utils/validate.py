from typing import Optional, Union
import json
from datetime import datetime

from utils.exmaples_error import not_valid_input_text, not_valid_input_data

def compare_input_format(input_data: str) -> Optional[dict]:
    try:
        data = json.loads(input_data)
    except Exception:
        return None
    return data

def compare_input_range_data(input_data: dict) -> Optional[dict]:
    dt_from = input_data.get('dt_from')
    dt_upto = input_data.get('dt_upto')
    if dt_from and dt_upto:
        try:
            formatted_dt_from = datetime.strptime(dt_from, '%Y-%m-%dT%H:%M:%S')
            formatted_dt_upto = datetime.strptime(dt_upto, '%Y-%m-%dT%H:%M:%S')
        except Exception:
            return None
        if formatted_dt_upto > formatted_dt_from:
            input_data['dt_from'] = formatted_dt_from
            input_data['dt_upto'] = formatted_dt_upto
            return input_data
    return None

def compare_group_type(input_data: dict) -> bool:
    sample_data = {'month': True, 'day': True, 'hour': True}
    if sample_data.get(input_data.get('group_type')):
        return True
    return False

def validate_input_data(input_text: str) -> Union[dict, str]:
    # проверка, что входные данные в нужном формате
    data = compare_input_format(input_text)
    if not data:
        return f'Невалидный запос. Пример запроса: {not_valid_input_text}'
    # проверка корректности введеной даты
    data = compare_input_range_data(data)
    if not data:
        return f'Допустимо отправлять только следующие запросы: {not_valid_input_data}'

    # провекрка значения group_type
    status_group_type = compare_group_type(data)
    if not status_group_type:
        return f'Допустимо отправлять только следующие запросы: {not_valid_input_data}'

    return data