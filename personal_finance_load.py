import psycopg2

conn = psycopg2.connect('postgresql://neondb_owner:npg_AYT3EPR9nOlv@ep-shy-wind-ad7mx136-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require')
cur = conn.cursor()
# cur.execute("""
#             CREATE TABLE IF NOT EXISTS daily_finance(
#             year INTEGER,
#             month VARCHAR(20),
#             report_day DATE,
#             income_type VARCHAR(50),
#             income_amount FLOAT,
#             expense_type VARCHAR(60),
#             expense_amount FLOAT);
#     """)

cur.execute("""
            INSERT INTO daily_finance (year, month, report_day, income_type, income_amount, expense_type, expense_amount)
            values (2023, 'March', '10-03-2023','RD Int', 357.00, 'NA', 0.0);
            """)

cur.execute("select * from daily_finance;")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()