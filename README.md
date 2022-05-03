<p align="center"><a href="#"><img src="python.png" width="200"></a></p>

# Parse Compras públicas!

Este programa foi desenvolvido para salvar vidas.

Ele formata as planilhas de compras publicas para o jeito perfeito para importar para o banco de dados

  

como usar:

- coloque todas as planilhas que vc precisará formatar em uma pasta chamada planilhas;

- certifique-se de que elas estão em ".csv";

- a partir desse ponto, se vc já tiver rodado o programa no mesmo dia, a execução anterior será excuida;

- entre na pasta do programa e use o cmd ou vc code e execute "py init.py". Voce verá varios numeros e espero que 0 erros;

- caso tenha dado certo, vai aparecer uma planilha na pasta resultado (os valores de data e valor da operação devem estar no padrao americano) (use o notepad ++ pra fazer a verificação);

- abra o DBeaver e entre na conexao db_portaltransparencia vá em tables e entre clique com o botao direito, vá em import e selecione csv, abra resultado-data-de-execucao, certifique-se que o column delimiter é ";";

- agora voce está na aba tables mapping, expanda a souce e veja se todas as colunas estão com o mappin = existing;

- clique em preview data, deve estar tudo separado bonitinho;

- clique em next e depois em proceed ou start.