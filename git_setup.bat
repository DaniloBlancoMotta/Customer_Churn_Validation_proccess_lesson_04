@echo off
echo Configurando repositorio Git para Customer Churn Analysis...

:: Inicializar repositorio Git
git init

:: Adicionar todos os arquivos
git add .

:: Fazer commit inicial
git commit -m "Initial commit: Customer Churn Feature Importance Analysis"

:: Adicionar repositorio remoto (substitua pelo nome do seu repositorio)
echo.
echo IMPORTANTE: Crie um novo repositorio no GitHub primeiro!
echo Sugestao de nome: customer-churn-analysis
echo.
echo Depois execute:
echo git remote add origin https://github.com/DaniloBlancoMotta/customer-churn-analysis.git
echo git branch -M main
echo git push -u origin main

pause