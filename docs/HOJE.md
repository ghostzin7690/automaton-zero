# AUTOMATON V4 — GUIA PARA CRIAR HOJE

## Objetivo

Construir um agente cloud-first que execute este ciclo:

PESQUISA → OPORTUNIDADE → MVP → PDF → VENDA → MÉTRICAS → APRENDIZADO → ESCALA

O servidor é o cérebro. O Android é o painel e recebe notificações.

## 1. Backend local

Instale Python 3.12.

```bash
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
```

Edite `.env`:

```text
GROQ_API_KEY=sua_chave
RUN_TOKEN=uma_senha_forte
MODE=approval
```

Rode:

```bash
uvicorn app.main:app --reload
```

Abra `http://127.0.0.1:8000/dashboard`.

## 2. Primeira pesquisa

Clique **Executar pesquisa**.

O Research Engine coleta sinais de mercado e a IA transforma evidências em candidatos.

A pesquisa acontece antes da criação do produto.

## 3. Validação

Score inicial:
- 70+ = candidato a MVP;
- abaixo disso = pesquisar mais.

É um parâmetro inicial, não garantia de vendas.

## 4. Produto

Clique **Criar MVP**.

O Product Factory gera nome, promessa, módulos, copy, hooks e PDF.

## 5. Kiwify

A Kiwify possui API pública e webhooks.

Na Kiwify:
- Apps → API → criar API Key;
- Apps → Webhooks → criar Webhook;
- URL do webhook: `https://SEU-APP.onrender.com/api/webhooks/kiwify`.

A primeira versão guarda o checkout URL no Automaton. Se algum endpoint de criação/publicação não estiver disponível para a operação desejada, faça essa etapa manualmente e depois conecte o checkout. O núcleo continua automático.

## 6. Experimentos

Registre impressões, cliques, vendas, receita e custo.

Exemplo:

```text
1000 impressões
100 cliques
10 vendas
R$199 receita
R$20 custo
=> SCALE_WINNER
```

## 7. AUTO

Comece em `MODE=approval`.

Depois de validar o ciclo completo, mude para `MODE=auto`.

Mesmo em AUTO, mantenha aprovação humana para gasto de dinheiro, dados bancários, exclusões destrutivas, credenciais e ações que uma plataforma exigir.

## 8. Render

1. Crie GitHub.
2. Suba o projeto.
3. Crie PostgreSQL no Render.
4. Crie Web Service.
5. Root Directory: `backend`.
6. Build: `pip install -r requirements.txt`.
7. Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
8. Configure secrets.
9. Deploy.
10. Teste `/health` e `/dashboard`.

Não dependa de SQLite/local files para persistência no Render Free.

## 9. Android

Abra `android` no Android Studio e troque `BASE_URL` pelo domínio do Render.

Depois adicione Firebase/FCM para push. O app não hospeda o Automaton; se o celular desligar, o servidor continua trabalhando.

## 10. Ordem das evoluções

V4.1: FCM + fila + scheduler + Kiwify mais completa.
V4.2: Instagram/TikTok oficiais.
V4.3: armazenamento S3/R2 + imagens/vídeos.
V5: múltiplos agentes, memória e alocação automática.

## Regra principal

Não crie centenas de produtos no escuro. Pesquise, encontre evidência, crie pequeno, teste, meça, aprenda e só então escale.
