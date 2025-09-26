import mariadb
import sys


try:

    conn = mariadb.connect(
        user='root',
        password='31142611',
        port=3306,
        database='alves_motors'
    )

except mariadb.Error as e:
    print(f'Erro ao conectar ao MariaDB: {e}')
    sys.exit(1)


def create_table():
    cur = conn.cursor()
    cur.execute("""
        create table if not exists veiculos (
            id integer primary key auto_increment,
            modelo text,
            marca text,
            cor text,
            ano integer
        )
        """)


def add_veiculo(modelo, marca, cor, ano):
    cur = conn.cursor()
    cur.execute('insert into veiculos (modelo, marca, cor, ano) values (?, ?, ?, ?)',
                (modelo, marca, cor, ano))
    conn.commit()


def listar_veiculos():
    cur = conn.cursor()
    cur.execute('select modelo, marca, cor, ano from veiculos')
    return cur.fetchall()  # busca todas as linhas em uma tabela


def atualizar_veiculos():
    pass


def excluir_veiculo(id):
    # exclui o veiculo com base no id
    cur = conn.cursor()
    cur.execute('delete from veiculos where id = ?', (id,))
    conn.commit()
