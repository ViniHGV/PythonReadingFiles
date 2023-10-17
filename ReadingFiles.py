import sqlite3

connector = sqlite3.connect("readingFiles.db")
cursor = connector.cursor()

CodProduto = []
NomeProduto = []
UnidadeComercializacao = []
ModoControleEstoque = []
QtdEstoque = []
PrecoUnitário = []
MargemLucro = []

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

SQL = """
  CREATE TABLE IF NOT EXISTS Produtos
  (
  cod integer primary key,
  nomeProduto string,
  unidadeComercializacao string,
  modoControleEstoque string,
  quantidadeEstoque numeric,
  precoUnitario numeric,
  MargemLucro numeric
  )
"""
cursor.execute(SQL)

print("\nTabela Produtos Criada com sucesso🚀\n")

for i in range(len(CodProduto)):
    Sql = f"""
      insert into Produtos (cod, nomeProduto, unidadeComercializacao, modoControleEstoque, quantidadeEstoque, precoUnitario, MargemLucro)
      values ({CodProduto[i]},'{NomeProduto[i]}', '{UnidadeComercializacao[i]}', '{
        ModoControleEstoque[i]}', {QtdEstoque[i]}, {PrecoUnitário[i]}, {MargemLucro[i]})
    """
    cursor.execute(Sql)

print("\nOs valores foram inseridos na tabela Produtos🚀\n")


AnoVenda = []
MesVenda = []
DiaVenda = []
CodigoProduto = []
QuantidadeVendida = []
PrecoVenda = []

arq = open("vendas.txt", "r")
s = arq.readline().rstrip()
while s != '':
    s = s.split(';')
    AnoVenda.append(int(s[0]))
    MesVenda.append(int(s[1]))
    DiaVenda.append(int(s[2]))
    CodigoProduto.append(int(s[3]))
    QuantidadeVendida.append(float(s[4]))
    PrecoVenda.append(float(s[5]))
    s = arq.readline().rstrip()
arq.close()

SQL = """
  CREATE TABLE IF NOT EXISTS Vendas(
  id integer primary key autoincrement,
  anoVenda integer,
  mesVenda integer,
  diaVenda integer,
  codProduto integer,
  qtdVendida numeric,
  precoVenda numeric
  )
"""
cursor.execute(SQL)
print("\nTabela Vendas Criada com sucesso🚀\n")


for i in range(len(CodigoProduto)):
    Sql = f"""
      insert into Vendas (anoVenda, mesVenda, diaVenda, codProduto, qtdVendida, precoVenda)
      values ({AnoVenda[i]},{MesVenda[i]}, {DiaVenda[i]}, {
        CodigoProduto[i]}, {QuantidadeVendida[i]}, {PrecoVenda[i]})
    """
    cursor.execute(Sql)

print("\nOs valores foram inseridos na tabela Vendas🚀\n")

connector.commit()
cursor.close()
connector.close()
