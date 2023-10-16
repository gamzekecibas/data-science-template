def to_categorical(dataframe):
    """
    A function to replace categories with numbers from 0 to N
    for unique string values in all columns of a dataframe.
    """
    for column_name in dataframe.columns:
        if dataframe[column_name].dtype == "object":
            unique_values = dataframe[column_name].unique().tolist()
            unique_values.sort()
            unique_values_dict = dict(zip(unique_values, range(len(unique_values))))
            dataframe[column_name] = dataframe[column_name].replace(unique_values_dict)

    return dataframe
