![Static Badge](https://img.shields.io/badge/Em%20Desenvolvimento-maker?style=for-the-badge&color=orange)

<div align="center">
  <h1> Swosh Scan </h1>
</div>
<br>

<h2>📄Sobre</h2>

<p>Este programa foi desenvolvido em Python para monitorar continuamente a velocidade de download, upload e ping de uma rede. O objetivo principal é coletar e exibir os dados de desempenho da rede em intervalos regulares, permitindo que o usuário acompanhe o comportamento da conexão ao longo do tempo. O programa também permite a finalização da coleta de dados através de um DataFrame.</p>

<h2>📚 Bibliotecas Usadas</h2>

<p>É preciso das seguintes bibliotecas para o funcionaemnto do programa:</p>

<p><strong>Speedtest-cli:</strong> Para coleta de informações sobre a rede conectada;</p>

```bash
pip install speedtest-cli
```
<p><strong>Pandas:</strong> Com os dados coletados, será gerado um DataFrame onde podemos organiza-los;</p>

```bash
pip install pandas
```

<h2>⚙️ Funcionamento: </h2>

<p>
  O programa executa 5 testes do seu computador com a rede conectada, medindo a velocidade media de download, upload e a latência (ping) da internet.
  Depois, são apresentadas as médias coletadas de cada teste e a media geral de velociade da rede que foi testada.
  O usuário pode analizar os saltos e qual o melhor servidor disponível. Caso queira, ele pode salvar os dados que foram coletados e monitorar se está havendo perda de desempenho na rede.
</p>