from fordev.generators import people
import json


#print(people(sex='F', age=30, uf_code='AC'));

# Converte o JSON para uma String
# jsonToString = json.dumps(people(sex='F', age=24, uf_code='RJ'))
# print(type(jsonToString))

json_object = people(sex='F', age=30, uf_code='AC')
values = [list(x.values()) for x in json_object]
#print(values)

# Cria uma lista com os nomes das colunas
nome_das_colunas = [
    'profissional_nome', 
    'profissional_cpf',
    'profissional_rg',
    'profissional_endereco_fk'
]

# String para SQL
sql_string = ""

for i, record in enumerate(values):
    # lista vazia para os values
    values_list = []

    # Acrescenta cada valor para a lista de values_list
    for v, val in enumerate(record):
        if type(val) == str:
            val = "'{}'".format(val.replace("'", "''"))
        values_list += [str(val)]

    # Acrescenta os parentes por causa do SQL
    sql_string += "(" + ", ".join(values_list) + "),\n"


sql_string = sql_string[:-2] + ";"

# Concatena as strings
nome_da_tabela = "profissional"
sql_insert_montado = "INSERT INTO %s (%s)\nVALUES\n%s" % (nome_da_tabela, ', '.join(nome_das_colunas), sql_string)

print("\nSQL string:\n\n")
print(sql_insert_montado)