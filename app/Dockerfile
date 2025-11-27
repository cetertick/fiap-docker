# ---------- STAGE 1: BUILDER ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Copia somente requirements para cache mais eficiente
COPY requirements.txt .

# Instala dependências no diretório do usuário root
RUN pip install --user -r requirements.txt


# ---------- STAGE 2: RUNTIME ----------
FROM python:3.12-slim AS runtime

# Cria o usuário não-root
RUN useradd -m userapp

# Cria o diretório /app com o owner correto
RUN mkdir -p /app && chown -R userapp:userapp /app

WORKDIR /app

# Copia dependências instaladas no builder
COPY --from=builder /root/.local /home/userapp/.local

# Copia o código da aplicação
COPY . /app

# Ajusta permissões finais
RUN chown -R userapp:userapp /app

# Configura PATH para dependências instaladas via pip --user
ENV PATH="/home/userapp/.local/bin:$PATH"

# Troca para o usuário seguro
USER userapp

EXPOSE 5000

CMD ["python", "src/app.py"]

