import dask.dataframe as dd


def merge_via_bq():
    pass


def merge_via_spark():
    pass


def merge_via_ray():
    pass


def merge_via_dask(a, b):
    a = dd.from_pandas(a, npartitions = 100)
    b = dd.from_pandas(b, npartitions = 100)



def main():
    a = pd.read_parquet()
    b = pd.read_parquet()
