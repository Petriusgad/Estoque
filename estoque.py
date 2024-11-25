estoque =[]

def cadastro():
    #cada cadastro é armazenado em produto e adicionado no estoque
    produto = {}
    
    a = int(input('Digite o código do produto: '))

    for item in estoque:
        if item['ID']==a:
            print(f'O código{a} já existe no sistema')
            return
    
    produto['ID']=a
    produto['Nome']=input('Digite o nome do produto: ')
    produto['Preço']=float(input('Digite o preço do produto: '))
    produto['Quantidade']=int(input('Digite a quantidade do produto: '))

    estoque.append(produto)
    print('Cadastrado com sucesso')

def consulta():
    pesquisa= int(input('Digite o código: '))

    for item in estoque:
        if item['ID']==pesquisa:
            print(f'O nome do produto é {item["Nome"]}, seu preço é {item["Preço"]} R$ e sua quantidade é {item["Quantidade"]} unidades')
            return
    
    print(f'O código {pesquisa} não está cadastrado no sistema')

def atualizacao():
    atualiza = int(input('Digite o código do produto a ser atualizado: '))

    for item in estoque:
        if item['ID']==atualiza:
            item['Nome']=input('Digite o novo nome do produto: ')
            item['Preço']=float(input('Digite o novo preço do produto: '))
            item['Quantidade']=int(input('Digite a nova quantidade do produto: '))
            print('Valores atualizados com sucesso!')
            return
    print(f'O código {atualiza} não se encontra no sistema')

def excluir():
    apaga = int(input('Digite o código do produto a ser apagado: '))
    for item in estoque:
        if item['ID']==apaga:
            item['Nome'] = ''
            item['Preço'] = ''
            item['Quantidade'] = ''
            item['ID'] = ''

            print('Produto apagado com sucesso')
            return
    print(f'O código {apaga} não está registrado no sistema')

while True:
    print('Insira a opção desejada:\n ')
    print('1: Cadastro\n')
    print('2: Consulta\n')
    print('3: Atualizar produto\n')
    print('4: Excluir produto\n')
    print('Digite qualquer outra tecla para sair do programa\n')
    
    option = int((input('Operação: ')))

    if option == 1:
        cadastro()
        continue
    if option == 2:
        consulta()
        continue
    if option == 3:
        atualizacao()
        continue
    if option == 4:
        excluir()
        continue
    else:
        print('Fechando o programa..')
        break


