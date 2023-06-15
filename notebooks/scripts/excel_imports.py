import pandas as pd

def append_sheets_with_organ_column(file_path):

    # Read all sheets into a dictionary of DataFrames
    sheets = pd.read_excel(file_path, sheet_name=None)

    # Concatenate all sheets into a single DataFrame
    concatenated_data = pd.concat(sheets.values())

    # Drop 'Unnamed' columns
    unnamed_columns = [col for col in concatenated_data.columns if col.startswith('Unnamed')]
    concatenated_data.drop(columns=unnamed_columns, inplace=True)

    # Print number of NaN values in each column, column element datatypes
    nan_counts = concatenated_data.isnull().sum()
    for column, count in nan_counts.items():
        column_data = concatenated_data[column]  # Get the column itself
        column_type = column_data.dtype  # Get the datatype of column elements
        print(f"Column '{column}': {count} NaN values; datatype: {column_type}")

    # Count rows with NaN values
    rows_with_nan = concatenated_data.isnull().any(axis=1).sum()
    print(f"\nNumber of rows with at least one NaN value: {rows_with_nan} of {len(concatenated_data.index)}")
    print("\nOrgans: " + ", ".join(list(set(concatenated_data["Organ"]))))
    concatenated_data['PMID'] = concatenated_data['PMID'].astype(str)
    concatenated_data['PEG cover'] = concatenated_data['PEG cover'].astype(str)
    concatenated_data['Ligand'] = concatenated_data['PEG cover'].astype(str)
    nps = "\n- ".join(list(set(concatenated_data['NP_Type'])))
    print(f'\nIncluded NPs: \n- {nps}')

    return concatenated_data

def describe_df(df):
    # Print number of NaN values in each column, column element datatypes
    nan_counts = df.isnull().sum()
    for column, count in nan_counts.items():
        column_data = df[column]  # Get the column itself
        column_type = column_data.dtype  # Get the datatype of column elements
        print(f"Column '{column}': {count} NaN values; datatype: {column_type}")

    # Count rows with NaN values
    rows_with_nan = df.isnull().any(axis=1).sum()
    print(f"\nNumber of rows with at least one NaN value: {rows_with_nan} of {len(df.index)}")
    print("\nOrgans: " + ", ".join(list(set(df["Organ"]))))
    nps = "\n- ".join(list(set(df['NP_Type'])))
    print(f'\nIncluded NPs: \n- {nps}')
    shapes = "\n- ".join(list(set(df['NP_Shape'])))
    print(f'\nShapes: \n- {shapes}')
    ligands = "\n- ".join(list(set(df['Ligand'])))
    print(f'\nLigands used for imaging: \n- {ligands}')
    coating = "\n- ".join(list(set(df['PEG cover'])))
    print(f'\nCoating (PEG covers): \n- {coating}')

 