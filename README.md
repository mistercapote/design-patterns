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
1.  - Creator: `PaymentProcessor`. 
    - Concrete Creator: `PixProcessor`, `CreditCardProcessor` e `BoletoProcessor`. 
    - Product: `Payment`.   
    - Concrete Product: `PixPayment`, `CreditCardPayment` e `BoletoPayment`.

2. Uma cadeia de if/elif caracteriza apenas uma fábrica simples. O padrão Factory Method fundamenta-se em polimorfismo e herança: a classe base define a operação com um método abstrato de criação e as subclasses decidem qual classe concreta instanciar.   

3. Nenhuma classe existente precisa de ser alterada. Apenas se estende o sistema criando uma nova subclasse de Payment e uma nova subclasse de PaymentProcessor, cumprindo o princípio Open/Close do SOLID.  


### 4. Famílias por canal

1. Porque ambos variam juntos em função do contexto do canal de venda (WEB, MOBILE ou KIOSK), exigindo interfaces e comportamentos correspondentes e coerentes entre si na mesma plataforma.   

2. Garante a criação de objetos compatíveis de uma mesma família sem misturar implementações.

3. Porque canal e forma de pagamento variam de forma independente. Acoplar o pagamento à fábrica do canal violaria o princípio de responsabilidade única (SRP).   

### 5. Seleção de fábrica e alteração do sistema

1.  - Arquivos criados: `channels/kiosk.py`, contendo `KioskCheckout`, `KioskNotification` e `KioskFactory`. Nenhum ficheiro do sistema foi alterado.   

2. São compatíveis com o OCP porque o sistema foi estendido com novas classes sem modificar o código de get_channel_factory, das abstrações base ou dos canais existentes, permanecendo fechado para alteração e aberto para extensão

### 6. Responsabilidades e integração

1. A classe coordenadora `OrderService` tem como responsabilidade principal apenas orquestrar o fluxo, chamando
as demais classes e funções na ordem correta.

- AppConfig: Armazenar as informações do ambiente e garantir o acesso a uma única instância global compartilhada.   

- OrderBuilder: Isolar a complexidade de criar os pedidos passo a passo, lidando com a validação de atributos obrigatórios e a adição de opcionais.   

- OrderService: Orquestrar o fluxo principal (construção, checkout, pagamento, notificação) delegando a execução aos componentes adequados, sem acoplar-se a implementações concretas

- PaymentProcessor: Ele atua como o componente base que define o fluxo padrão de cobrança, delegando a criação da forma de pagamento exata para as subclasses. A responsabilidade dele é isolar a lógica de processamento, garantindo que o sistema não precise saber os detalhes concretos de como o PIX ou o Cartão são instanciados.

- get_channel_factory: selecionar e retornar qual factory deve ser usada para o canal informado.

- Channel Factory (e suas filhas): Elas agrupam a criação do checkout e da notificação, garantindo que os objetos criados pertençam à mesma família (ou seja, evita que o sistema misture um checkout WEB com uma notificação MOBILE, por exemplo).

- Order e Product: Guardam os dados essenciais e as regras básicas do negócio (como somar o total).

- Payment (e filhas como PixPayment): Executam a ação específica daquela forma de pagamento.

- Checkout e Notification (e suas filhas): Isolam a lógica visual ou de envio de mensagens de cada canal.

2.  Focando em `OrderBuilder` e `ÀppConfig `OrderBuilder`: Se a regra de negócio mudar e o sistema passar a exigir, por exemplo, que "endereço" vire um atributo obrigatório para fechar a compra, a validação essa validação apenas dentro do método .build() do OrderBuilder.  O `OrderService` ou as factorys continuariam funcionando sem nem precisar saber dessa nova regra. 
- `AppConfig`: Se no futuro o sistema precisar de uma variável nova, como a URL de um banco de dados ou um limite de tentativas, você adiciona isso diretamente no AppConfig. O resto do sistema (OrderService, etc.) não precisará sofrer nenhuma alteração. 
 - `PixPayment`: Se a APi do banco passar a exigir um novo parâmetro de autenticação exclusivo para o PIX, essa mudança será feita direaframente no `PixPayment`, não afetando `PaymentProcessor` nem `OrderService

3. Atualmente os canais (WEB, MOBILE) são registrados escrevendo as chamadas da função diretamente no código-fonte.  Uma decisão de projeto que poderia ser diferente é o registro estático (hardcoded) das fábricas de canais diretamente no código-fonte. Como alternativa, o sistema poderia ser adaptado para ler a lista de canais disponíveis a partir de um arquivo de configuração externo (como um arquivo JSON ou .env) durante a sua inicialização. A consequência direta dessa mudança seria um aumento significativo na flexibilidade da arquitetura, permitindo a adição de novos canais (como o KIOSK) apenas inserindo uma linha nesse arquivo externo, sem a necessidade de um desenvolvedor abrir e alterar o código-fonte original da aplicação.

