import json
import pandas as pd
import re


def sentence_case(string: str) -> str:
    if string != '':
        result = re.sub('([A-Z])', r' \1', string)
        return result[:1].upper() + result[1:].lower()
    return ""


def df_to_muidatagrid(dataframe=None, csv_file_path='', index_col='id'):

    if csv_file_path == "":
        df = dataframe
    else:
        df = pd.read_csv(csv_file_path, index_col=index_col)

    output_dict = {'columns': [{
        "field": "id",
        "headerName": "ID",
        "width": 90
    }]}

    for c in list(df.columns):
        output_dict['columns'].append({
            "field": c,
            "headerName": sentence_case(c),
            "width": 100
        })

    row_dict = df.to_dict('records')
    output_dict['rows'] = []
    ind = list(df.index)
    for e, (i, r) in enumerate(zip(ind, row_dict)):
        r['id'] = i
        output_dict['rows'].append(r)

    jsonFile = open("program_output.json", "w")
    jsonFile.write(json.dumps(output_dict))
    jsonFile.close()
