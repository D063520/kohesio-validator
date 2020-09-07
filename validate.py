from tableschema import Table

table = Table("template.csv", schema="schema.json")
table.schema.valid
# True

for row in table.iter():
  print(row)