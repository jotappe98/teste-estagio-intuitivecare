-- 1. Lista de operadoras ordenadas pelo total de despesas (decrescente)
SELECT razao_social, uf, total_despesas
FROM despesas_operadoras
ORDER BY total_despesas DESC;

-- 2. Top 10 operadoras com maior total de despesas
SELECT razao_social, uf, total_despesas
FROM despesas_operadoras
ORDER BY total_despesas DESC
LIMIT 10;

-- 3. Total de despesas agrupadas por UF
SELECT uf, SUM(total_despesas) AS total_despesas_uf
FROM despesas_operadoras
GROUP BY uf
ORDER BY total_despesas_uf DESC;

-- 4. Operadoras com média trimestral acima de um valor específico
SELECT razao_social, uf, media_trimestral
FROM despesas_operadoras
WHERE media_trimestral > 1000000
ORDER BY media_trimestral DESC;

-- 5. UF com maior volume total de despesas
SELECT uf, SUM(total_despesas) AS total_despesas_uf
FROM despesas_operadoras
GROUP BY uf
ORDER BY total_despesas_uf DESC
LIMIT 1;