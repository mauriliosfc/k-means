# k-means
Trabalho prático de tópicos especiais
# Agrupar produtos e seus consumidores
A ideia seria obter grupos de consumidores e seus tipos de produtos para conseguir extrair um nicho de clientes e realizar um marketing direcionado as estes consumidores.
# Critério de sucesso
Repetir o calculo dos centróides até que não sejam mais modificados.
# Agrupamento
Nesse caso agrupar os dados permite tomar decisões especificas para cada perfil (cluster), além de conseguir encontrar grupos que não eram visíveis e dassa forma conseguir direcionar o marketing a esses perfis de consumidores.

# Numero de clusters
O algoritmo foi executado algumas vez com numero de clusters diferentes até que houvesse uma diferença maior entre os clusters, pois nesse modelo de dados é interessante perceber clusters mais diversos para poder usar as informações para cada caso. No fim chagamos ao valor de 5 clusters.

# Os parâmetros do método de clusterização
Os parâmetros de 5 clusterização, implicam diretamente nos resultados, se o numero for muito baixo podemos ter pouco conjuntos que não serão específicos e não representaram de forma correta um determinado nicho, porem se o numero for alto as diferenças entre clusters se tornam muito pequenas. Então é preciso achar um equilíbrio em que as observações que formam cada agrupamento sejam o mais homogêneas possível e que os agrupamentos formados sejam o mais diferentes um dos outros.

# Avaliação dos resultados
![Gráfico](https://github.com/mauriliosfc/k-means/blob/master/km1)

* cluster 0 - clientes que gastão pouco com cada tipo de produto.
* cluster 1 - clientes que não gastão tanto, mas tem compram mais Leite e produtos de mercearia.
* cluster 2 - clientes que gastão mais porém com foco em produtos frescos.
* cluster 3 - clientes que não gastão tanto mais também com foco em produtos frescos.
* cluster 4 - clientes que com gasto eleva e mais diversificado.

# Conclusões e resultados
Como vimos no gráfico acima, o que o algoritmo fez  foi identificar clientes com comportamentos similares. Desta maneira, é possível fazer uma ação especial com os clientes que gastam mais com determinados alimentos.
