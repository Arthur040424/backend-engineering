import psycopg2

def get_connection():
  return psycopg2.connect(
    dbname="url_shortener",
    user="postgres",
    password="postgres",
    host="localhost"
  )

def get_url(short_code):
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute("SELECT long_url FROM urls WHERE short_code = %s", (short_code,))
  result = cursor.fetchone()
  cursor.close()
  conn.close()
  if result:
    return result[0]
  return "URL Not Found"

print(get_url("abc123"))
print(get_url("gh999"))
print(get_url("zzz999"))