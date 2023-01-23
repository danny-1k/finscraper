from typing import List


def construct_table_from_data(headers: List[str], table: List[str]) -> list:
    data = []

    if len(table) < 1 or len(headers) < 1:
        return []

    for i in range(len(table)//len(headers)):
        ticker_sub = {}
        for j, header in enumerate(headers):
            ticker_sub[header] = table[i*j]

        data.append(ticker_sub)

    return data