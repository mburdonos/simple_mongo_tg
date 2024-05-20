from json import dumps

not_valid_input_text = dumps(
    {
        "dt_from": "2022-09-01T00:00:00",
        "dt_upto": "2022-12-31T23:59:00",
        "group_type": "month",
    }
)

not_valid_input_data = ",".join(
    [
        dumps(
            {
                "dt_from": "2022-09-01T00:00:00",
                "dt_upto": "2022-12-31T23:59:00",
                "group_type": "month",
            }
        ),
        dumps(
            {
                "dt_from": "2022-10-01T00:00:00",
                "dt_upto": "2022-11-30T23:59:00",
                "group_type": "day",
            }
        ),
        dumps(
            {
                "dt_from": "2022-02-01T00:00:00",
                "dt_upto": "2022-02-02T00:00:00",
                "group_type": "hour",
            }
        ),
    ]
)
