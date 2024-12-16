# Exemplo de Pipeline CI/CD com Python

Este projeto demonstra um exemplo prático de um pipeline de Integração Contínua e Entrega Contínua (CI/CD) usando Python, testes automatizados, Docker e GitHub Actions. Ele foi desenvolvido para compor meu portfólio com boas práticas de desenvolvimento.

O pipeline automatiza as seguintes etapas:

1.  **Testes:** Executa os testes unitários a cada push em branches de feature, develop e main e em pull requests para o branch main, verificando se o código funciona como esperado. Também gera um relatório de cobertura de testes com `pytest-cov` e verifica a qualidade do código usando o linter `flake8`.
2.  **Build e Push da Imagem Docker:** Quando um merge é realizado no branch `main`, ou um push é diretamente efetuado para este branch, o pipeline cria uma imagem Docker da aplicação e a envia para o Docker Hub.

## Tecnologias Utilizadas:

*   **Python:** Linguagem de programação.
*   **pytest:** Framework de testes unitários.
*   **pytest-cov:** Plugin para gerar relatórios de cobertura de testes.
*   **flake8:** Linter para análise estática de código.
*   **Docker:** Plataforma de containerização.
*   **GitHub Actions:** Plataforma de CI/CD.
*   **Gitflow (Simplificado):** Estratégia de branching.

Competências:

Desenvolvimento com Python e implementação de testes automatizados.
Configuração e gestão de pipelines CI/CD utilizando GitHub Actions.
Uso de Docker para criação e publicação de containers.
Controle de versão e organização de branches com Git.

Acesse o pipeline completo na aba Actions deste repositório. A imagem Docker publicada está disponível em meu Docker Hub: https://hub.docker.com/repository/docker/millerjmatos/gitflow-pipeline-test
