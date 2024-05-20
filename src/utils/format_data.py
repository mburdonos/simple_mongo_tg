from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta

def create_structure(data: list, date_range: list) -> dict:
    result_data = {"dateset": [], "labels": date_range}
    local_data = {}
    for val in data:
        local_data.update({val.get('_id'): val.get('dataset')})
    for date_row in date_range:
        result_data["dateset"].append(local_data.get(date_row, 0))
    return result_data

def create_diapozone(data: dict) -> list:
    sample_date = {
        "month": "mo",
        "day": "%Y-%m-%dT00:00:00",
        "hour": "%Y-%m-%dT%H:00:00",
    }
    result_data = []
    date_from = data.get('dt_from')
    date_to = data.get('dt_upto')
    while date_from <= date_to:
        if data.get('group_type') == 'hour':
            result_data.append(date_from.strftime('%Y-%m-%dT%H:00:00'))
            date_from = date_from + timedelta(hours=1)
        elif data.get('group_type') == 'day':
            result_data.append(date_from.strftime('%Y-%m-%dT00:00:00'))
            date_from = date_from + timedelta(days=1)
        elif data.get('group_type') == 'month':
            result_data.append(date_from.strftime('%Y-%m-00T00:00:00'))
            date_from = date_from + relativedelta(months=+1)
    return result_data