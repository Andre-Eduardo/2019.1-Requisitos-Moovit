|Data|Versão|Descrição|Autor|
|:---|:---|:---|:----|
|27/04/2019|1.0|Criação do conteúdo |Arthur Rodrigues|


***<a name="Mapear Uma Linha De ônibus Dentro Do Veículo">Mapear uma linha de ônibus dentro do veículo</a>***

|Versão|1.0|
|--|:--|
|**Objetivo**|Mostrar o processo de como o usuário pode registrar informações geográficas para atualizar o [trajeto](./Lexicos#trajeto) de uma [linha](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L27---linha) |
|**Contexto**|Local = Todo o [trajeto](./Lexicos#trajeto) daquela [linha](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L27---linha) Tempo = Quando o [veiculo](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L66-Veiculo) sair da primeira [parada de onibus](./Lexicos#parada-de-onibus) até chegar a ultima<br>Pré-condição = Estar [a bordo](./Lexicos#a-bordo) , acesso a internet |
|**Ator(es)**|[usuario](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L65-Usu%C3%A1rio) [moovit](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L38---moovit) [veiculo](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L66-Veiculo) |
|**Recursos**|[aplicativo](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L03---aplica%C3%A7ao-mobile) [mobile](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L03---aplica%C3%A7ao-mobile) [gps](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L21---gps) funcionando [mapa](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L18---mapa) |
|**Episódios**|O [usuario](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L65-Usu%C3%A1rio) clica em mapeie sua [linha](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L27---linha) Quanto passar por uma [parada de onibus](./Lexicos#parada-de-onibus) clique no botão indicado<br>Quando terminar o [percurso](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L50---percurso) , selecione a [linha](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L27---linha) depois depois a [direção](./Lexicos#direcao) Envie os dados |
|**Exceções**|O onibus quebrar<br>O onibus ser obrigado a desviar a [rota](https://github.com/Andre-Eduardo/2019.1-Requisitos-Moovit/wiki/L58---rota) , devido a acidentes ou obras na pista |