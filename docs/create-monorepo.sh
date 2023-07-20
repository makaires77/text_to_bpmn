#!/bin/bash

# Nome padrão do monorepo e pacotes/subdiretórios
monorepo_name=${1:-"meu-monorepo"}
declare -a packages=("api" "app" "common" "models" "services" "utils")
declare -a sub_dirs=("src" "test" "doc")

# Cria o diretório do monorepo, se não existir
mkdir -p $monorepo_name

# Cria um diretório para cada pacote dentro do monorepo, se não existir
for package in "${packages[@]}"
do
  mkdir -p "$monorepo_name/$package"
done

# Para cada pacote, cria os subdiretórios, se não existirem
for package in "${packages[@]}"
do
  for sub_dir in "${sub_dirs[@]}"
  do
    mkdir -p "$monorepo_name/$package/$sub_dir"
  done
done