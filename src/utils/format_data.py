def create_structure(data: list) -> dict:
    dataset = []
    labels = []
    for val in data:
        dataset.append(val.get('dataset'))
        labels.append(val.get('_id'))
    return {"dataset": dataset, "labels": labels}