# API greatGrades

# FUNCIONALIDADE

A API _greatGrades_ é oferecida com a intenção de facilitar e agilizar o trabalho do professor, 
realizando correções de avaliações por intermédio do fornecimento de gabaritos; cálculo do peso 
diferenciado das questões; e, por fim, calculando a média de cada aluno e verificando quais 
foram aprovados, isto é, atingiram média maior ou igual a 7 (sete).

# COLETA DAS INFORMAÇÕES

A transferência dos dados é feita usando protocolo HTTP, verbo GET e recebe os dados no formato JSON. O aplicativo será implantado na URL: _greatGrades.com.br_. Esta documentação estará disponível também no _endpoint_:  _greatGrades.com.br/docs_.
_greatGrades_ não tem limite de provas podendo ser utilizado para 
  qualquer avaliação objetiva de gabarito fixo, independente do número de questões.

Abaixo exemplo de modelo JSON aceito:

```
{	
	"templates": [["a", "b", "c", "d"], ["a", "b", "c", "d", "e"]],
	"values": [[2, 3, 2, 3],	[3, 2, 1, 2, 2]],
	"students": {
		"Asterix":[["a", "b", "c", "d",], ["a", "c", "b", "d", "e"]],
		"Obelix": [["a", "b", "c", "d"], ["a", "c", "b", "d", "e"]],
		"Ideiafix": [["a", "b", "b", "d"], ["a", "b", "b", "d", "e"]],
		"Julius Caesar": [["a", "c", "b", "d"], ["a", "c", "b", "d", "e"]]		
	}
}
```
Os campos __templates__, __values__ e __students__ são obrigatórios, bem como o fornecimento de seus dados em vetores. Todavia, como dito, o funcionamento da API independe do número de vetores (número de avaliações) e da quantidade de dados (número de questões) neles.  

_greatGrades_ trabalha com avaliações com valor final 10 (dez). Isto obriga que cada vetor __values__ somem 10 (dez) no conjunto de seus pesos. O número máximo de alunos é 100.

# ENTREGA DO RESULTADO FINAL

_greatGrades_ entrega como resultado uma lista de aprovados, também em JSON no seguinte formato:
```
{
  "approved": [
    "Mussum",
    "Zacarias",
    "Dedé"
  ]
}
```

# MELHORAMENTOS

Relacionamos abaixo alguns melhoramentos possíveis e desejáveis:
- seleção de médias diferentes de 7;
- definição de pesos diferentes para cada avaliação;
- divulgação de médias finais e relação dos estudantes reprovados.


