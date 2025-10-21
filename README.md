# <img src="https://img.icons8.com/color/48/000000/bar-chart.png" width="24"/> Análise de Importância de Features - Customer Churn

## <img src="https://img.icons8.com/color/48/000000/target.png" width="20"/> Objetivo

Este projeto implementa uma análise de importância de features para predição de churn de clientes usando dados de telecomunicações. O objetivo é identificar quais características dos clientes são mais relevantes para determinar se eles irão cancelar o serviço.

## <img src="https://img.icons8.com/color/48/000000/folder-tree.png" width="20"/> Estrutura do Projeto

```
Lesson4/
├── 📄 feature_importance.py    # Script principal de análise
├── 📊 telco_customer_churn.csv # Dataset de clientes
├── 📓 notebook.ipynb          # Jupyter notebook
├── 🌐 index.html              # Visualização web
├── 📦 archive.zip             # Arquivo compactado
└── 📖 README.md               # Este arquivo
```

## <img src="https://img.icons8.com/color/48/000000/settings.png" width="20"/> Tecnologias Utilizadas

- **Python 3**
- **pandas** - Manipulação de dados
- **numpy** - Operações numéricas
- **matplotlib** - Visualização de dados
- **scikit-learn** - Machine Learning

## <img src="https://img.icons8.com/color/48/000000/checklist.png" width="20"/> Pré-requisitos

```bash
pip install pandas numpy matplotlib scikit-learn
```

## <img src="https://img.icons8.com/color/48/000000/rocket.png" width="20"/> Como Executar

1. **Clone ou baixe o projeto**
2. **Navegue até o diretório do projeto**
3. **Execute o script principal:**

```bash
python feature_importance.py
```

## <img src="https://img.icons8.com/color/48/000000/database.png" width="20"/> Dataset

O dataset `telco_customer_churn.csv` contém informações sobre clientes de uma empresa de telecomunicações, incluindo:

- **Dados demográficos**: gênero, idade, dependentes
- **Serviços contratados**: telefone, internet, streaming
- **Informações da conta**: tipo de contrato, método de pagamento, valores
- **Target**: churn (se o cliente cancelou o serviço)

## <img src="https://img.icons8.com/color/48/000000/artificial-intelligence.png" width="20"/> Escolha do Modelo

### Por que Regressão Logística?

A **Regressão Logística** foi escolhida por várias razões estratégicas:

#### <img src="https://img.icons8.com/color/48/000000/checkmark.png" width="16"/> Vantagens

1. **Interpretabilidade**: Os coeficientes podem ser facilmente interpretados como importância das features
2. **Probabilidades**: Fornece probabilidades de churn, não apenas classificações
3. **Eficiência**: Rápido para treinar e fazer predições
4. **Baseline sólida**: Excelente modelo de referência para problemas de classificação binária
5. **Robustez**: Menos propenso a overfitting comparado a modelos mais complexos
6. **Coeficientes lineares**: Permitem análise direta da importância das features

#### <img src="https://img.icons8.com/color/48/000000/bullseye.png" width="16"/> Adequação ao Problema

- **Classificação binária**: Churn (sim/não) é um problema binário perfeito para logística
- **Features categóricas**: Funciona bem com variáveis dummy criadas pelo DictVectorizer
- **Análise de importância**: Os coeficientes fornecem insights diretos sobre quais features mais influenciam o churn

## <img src="https://img.icons8.com/color/48/000000/test-tube.png" width="20"/> Metodologia de Teste

### Divisão dos Dados

```
Dataset Original (100%)
├── Treino Completo (80%)
│   ├── Treino (60% do total)
│   └── Validação (20% do total)
└── Teste (20%)
```

### Estratégia de Validação

1. **Train-Validation Split**: 75%-25% do conjunto de treino
2. **Random State**: Fixado em 1 para reprodutibilidade
3. **Stratificação implícita**: Mantém proporção de classes

### Por que essa Abordagem?

- **Validação robusta**: Permite avaliar o modelo antes do teste final
- **Prevenção de overfitting**: Validação independente do treino
- **Reprodutibilidade**: Random state fixo garante resultados consistentes

## <img src="https://img.icons8.com/color/48/000000/line-chart.png" width="20"/> Análise de Importância

### Metodologia

1. **Extração de coeficientes**: Utiliza `model.coef_[0]` da regressão logística
2. **Ranking por magnitude**: Ordena features pelo valor absoluto dos coeficientes
3. **Top 14 features**: Foca nas características mais relevantes
4. **Visualização**: Gráfico de barras horizontais para melhor legibilidade

### Interpretação dos Coeficientes

- **Coeficiente positivo**: Aumenta a probabilidade de churn
- **Coeficiente negativo**: Diminui a probabilidade de churn
- **Magnitude**: Indica a força da influência da feature

## <img src="https://img.icons8.com/color/48/000000/combo-chart.png" width="20"/> Resultados Esperados

O script gera:

1. **Gráfico de barras**: Visualização das top 14 features mais importantes
2. **Lista ordenada**: Ranking das features com seus coeficientes
3. **Insights acionáveis**: Identificação dos fatores críticos de churn

## <img src="https://img.icons8.com/color/48/000000/search.png" width="20"/> Features Tipicamente Importantes

Com base na natureza do dataset, espera-se que features relacionadas a:

- **Contratos mensais** (maior churn)
- **Métodos de pagamento** (cheque eletrônico = maior risco)
- **Serviços premium** (fiber optic, streaming)
- **Valores altos** (monthly charges)
- **Tempo de relacionamento** (tenure baixo = maior risco)

## <img src="https://img.icons8.com/color/48/000000/business.png" width="20"/> Aplicações Práticas

### Para o Negócio

1. **Identificação de clientes em risco**
2. **Estratégias de retenção direcionadas**
3. **Otimização de ofertas e promoções**
4. **Melhoria na experiência do cliente**

### Para Análise

1. **Baseline para modelos mais complexos**
2. **Feature engineering orientada**
3. **Insights para coleta de novos dados**
4. **Validação de hipóteses de negócio**

## <img src="https://img.icons8.com/color/48/000000/code.png" width="20"/> Notas Técnicas

- **DictVectorizer**: Converte dados categóricos em formato numérico
- **Max_iter=1000**: Garante convergência do algoritmo
- **Sparse=False**: Matriz densa para melhor performance com dados pequenos
- **Fillna(0)**: Tratamento de valores missing em TotalCharges

## <img src="https://img.icons8.com/color/48/000000/handshake.png" width="20"/> Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir melhorias
- Adicionar novas análises
- Otimizar o código

## <img src="https://img.icons8.com/color/48/000000/certificate.png" width="20"/> Licença

Este projeto é de uso educacional e está disponível sob licença MIT.

---

**Desenvolvido para análise de Customer Churn com foco em interpretabilidade e insights acionáveis.**