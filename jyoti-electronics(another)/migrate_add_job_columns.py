import sqlite3

conn = sqlite3.connect('jyoti_electronics.db')
c = conn.cursor()
def safe_add(col_sql):
    try:
        c.execute(col_sql)
        print("OK:", col_sql)
    except Exception as e:
        print("Skip / error:", e)

safe_add("ALTER TABLE job ADD COLUMN area TEXT;")
safe_add("ALTER TABLE job ADD COLUMN tv_model TEXT;")
safe_add("ALTER TABLE job ADD COLUMN repair_work TEXT;")
safe_add("ALTER TABLE job ADD COLUMN expense REAL DEFAULT 0.0;")
safe_add("ALTER TABLE job ADD COLUMN note TEXT;")
safe_add("ALTER TABLE job ADD COLUMN payment_mode TEXT;")

conn.commit()
conn.close()
print("Migration finished.")
