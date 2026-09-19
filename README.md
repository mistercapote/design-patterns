# design-patterns
Design Patterns — Atividade Avaliativa de Engenharia de Software

### 1. Configuração da aplicação
1. O Python invoca __init__ automaticamente sempre que __new__ devolve uma instância da classe. Como o __new__ devolve a mesma instância em chamadas subsequentes, o __init__ é executado novamente.

2. Como os módulos em Python são executados apenas na primeira importação e ficam em cache em sys.modules, definir variáveis globais diretamente num ficheiro .py cria um estado partilhado acessível via import em toda a aplicação sem recurso a classes.

3. Cria dependências ocultas e efeitos colaterais entre partes do código, o que prejudica o isolamento dos testes unitários, visto que a mutação num teste afeta os seguintes. 


### 2. Pedido e Builder
1. Builder: `OrderBuilder`. Objeto construído: `Order`.   
  
2. Embora o Python suporte parâmetros com valores default e por palavra-chave (kwargs), tornando a instanciação direta viável, a diferença é que o construtor direto gera assinaturas extensas e não permite validação gradual, enquanto o Builder separa a montagem passo a passo da validação das regras (como a obrigatoriedade do cliente) antes de consolidar a instância final.   
  
  
### 3. Pagamento e Factory Method
1. - Creator: `PaymentProcessor`. 
    - Concrete Creator: `PixProcessor`, `CreditCardProcessor` e `BoletoProcessor`. 
    - Product: `Payment`.   
    - Concrete Product: `PixPayment`, `CreditCardPayment` e `BoletoPayment`.

2. Uma cadeia de if/elif caracteriza apenas uma fábrica simples. O padrão Factory Method fundamenta-se em polimorfismo e herança: a classe base define a operação com um método abstrato de criação e as subclasses decidem qual classe concreta instanciar.   

3. Nenhuma classe existente precisa de ser alterada. Apenas se estende o sistema criando uma nova subclasse de Payment e uma nova subclasse de PaymentProcessor, cumprindo o princípio Open/Close do SOLID.  