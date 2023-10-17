import sqlite3

connector = sqlite3.connect("produtos.db")
cursor = connector.cursor()

CodProduto = []
NomeProduto = []
UnidadeComercializacao = []
ModoControleEstoque = []
QtdEstoque = []
PrecoUnitário = []
MargemLucro = []
'''
Lendo o arquivo Produtos
'''
arq = open("produtos.txt", "r")
s = arq.readline().rstrip()
while s != '':
    s = s.split(';')
    CodProduto.append(int(s[0]))
    NomeProduto.append(str(s[1]))
    UnidadeComercializacao.append(str(s[2]))
    ModoControleEstoque.append(str(s[3]))
    QtdEstoque.append(float(s[4]))
    PrecoUnitário.append(float(s[5]))
    MargemLucro.append(float(s[6]))
    s = arq.readline().rstrip()
arq.close()

# print(f"\n\nCódigo produto{"":3} Nome produto {
#       "":29}Unidade de Comercialização {"":4}Modo de controle do estoque")

SQL = """
  CREATE TABLE IF NOT EXISTS Produtos
  (
  cod integer primary key autoincrement,
  nomeProduto string,
  unidadeComercializacao string,
  modoControleEstoque string,
  quantidadeEstoque numeric
  )
"""
cursor.execute(SQL)
#  for i in range(len(CodProduto)):
