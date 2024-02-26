import pandas as pd

df0 = pd.read_csv("tbl0.tsv", sep="\t")
df1 = pd.read_csv("tbl1.tsv", sep="\t")
df2 = pd.read_csv("tbl2.tsv", sep="\t")
def pregunta_01():
    return df0.shape[0]


def pregunta_02():
    return df0.shape[1]


def pregunta_03():
    return df0['_c1'].value_counts().sort_index()


def pregunta_04():
    return df0.groupby('_c1')['_c2'].mean()


def pregunta_05():
    return df0.groupby('_c1')['_c2'].max()


def pregunta_06():
    return sorted(df1._c4.astype(str).str.upper().unique())


def pregunta_07():
    return df0.groupby('_c1')['_c2'].sum()


def pregunta_08():
    df0['suma'] = df0['_c2'] + df0['_c0']
    return df0


def pregunta_09():
    df0['year'] = df0['_c3'].str[:4]
    return df0

def pregunta_10():
    valores = df0.groupby('_c1')['_c2'].apply(lambda x: [str(i) for i in sorted(x)]).tolist()
    c2 = []

    for letra in valores:
        texto = ':'.join(letra)
        c2.append(texto)

    grouped_values = pd.DataFrame({'_c2': c2}, index=pd.Series(['A', 'B', 'C', 'D', 'E'], name='_c1'))
    return grouped_values

def pregunta_11():
    def join_sorted_values(row):
        values = sorted(map(str, row))
        return ','.join(values)

    grouped_values = df1.groupby('_c0')['_c4'].apply(join_sorted_values).reset_index()
    grouped_values.columns = ['_c0', '_c4']
    return grouped_values


def pregunta_12():
    def combine_values(row):
        values = [f"{a}:{b}" for a, b in zip(row['_c5a'], row['_c5b'].astype(str))]
        return ','.join(sorted(values))

    grouped_values = df2.groupby('_c0').apply(combine_values).reset_index()
    grouped_values.columns = ['_c0', '_c5']
    return grouped_values
def pregunta_13():
    merged_data = pd.merge(df0, df2, on='_c0', how='inner')

    grouped_data = merged_data.groupby('_c1').agg({'_c5b': 'sum'})
    result_series = grouped_data.squeeze()
    return result_series

