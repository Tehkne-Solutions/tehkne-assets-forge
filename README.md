# Tehkné Assets Forge

Pipeline open source e reutilizável da **Tehkné Solutions** para produção, validação, empacotamento e integração de assets de jogos.

## Objetivos

- padronizar packs de assets;
- validar imagens, manifests, checksums e budgets;
- gerar atlas e arquivos de runtime;
- produzir páginas de revisão e relatórios;
- integrar com GitHub Releases e engines de jogo;
- evitar placeholders, arquivos duplicados e falsas conclusões.

## Escopo inicial

A primeira implementação será extraída do pipeline criado para o Taijifu Masters, removendo dependências específicas do personagem Lian Wu e transformando contratos, comandos e workflows em componentes reutilizáveis.

## HOC world landmarks

O Forge também valida extensões authored de landmarks world-space do **Hexa Octarina Conquer**.

Contrato atual: `hoc/world-landmarks/v1`.

IDs neutros obrigatórios:

- `LANDMARK_CITY_NEUTRAL_01`
- `LANDMARK_MINE_NEUTRAL_01`

Validação do manifest:

```bash
tehkne-assets-forge validate-hoc-landmarks pack-manifest.json
```

Validação fail-closed do pacote materializado, incluindo existência e tamanho não-zero das artes:

```bash
tehkne-assets-forge validate-hoc-landmarks pack-manifest.json --root .
```

O contrato rejeita famílias semânticas incorretas, IDs duplicados, arquivos não renderizáveis e semântica de UI como `icon`, `badge`, `marker`, `portrait`, `card`, `frame`, `hud`, `logo` e `emblem`.

## Estrutura prevista

```text
src/
contracts/
plugins/
examples/
tests/
docs/
```

## Licença

A definir antes da primeira release pública.

Assinatura: **Tehkné Solutions**
