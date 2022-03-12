# python-mui
Tooling to export data to MUI Data Grid friendly forms


Theoretically there should be a one to one mapping between a panda dataframe and MUI datagrid. There may be occasions where we cannot automate the mapping from the DF to the required JSON blob (say for instance if there is some weird multi index stuff going on).

In this repository we are building a function/tool to generate the json data object required for MUI Data Grids from a pandas dataframe.