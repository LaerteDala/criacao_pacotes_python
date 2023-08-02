import textwrap

def menu():
    menu = """\n
        ================ MENU ================
        [d]\t Depositar
        [s]\t Sacar
        [e]\t Extrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\t Sair
        => """
    return input(textwrap.dedent(menu))
