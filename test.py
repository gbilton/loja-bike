import sqlite3

con = sqlite3.connect('loja.db')

cur = con.cursor()

q = ''' select c.nome, sum(p.preco) as total
        from vendas v
        join clientes c
        on v.id_cliente = c.id
        join produtos p
        on v.id_produto = p.id
        group by c.nome
        order by total desc
    '''

for row in cur.execute(q):
    print(row)
