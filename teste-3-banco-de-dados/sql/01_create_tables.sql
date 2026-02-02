CREATE TABLE IF NOT EXISTS despesas_operadoras (
id INT AUTO_INCREMENT PRIMARY KEY,
razao_social VARCHAR(255),
uf VARCHAR(2),
total_despesas DECIMAL(20, 2),
media_trimestral DECIMAL(20, 2),
desvio_padrao DECIMAL(20, 2)
);

