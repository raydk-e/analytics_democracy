import camelot
import pandas as pd
tables = camelot.read_pdf(
    "/home/deepak/projects/apr22.pdf",
    pages='all',
    flavor='stream',
    row_tol=6,
    column_tol=5,
    strip_text='\n'
)
print("number of tables", tables.n)
for i, table in enumerate(tables):
    print(f"table{i} rows : {len(table.df)}")

merged = pd.concat([t.df for t in tables])
print(merged)

merged.to_csv("/home/deepak/projects/apr22.csv")

