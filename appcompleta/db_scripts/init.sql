-- Cria a tabela se não existir
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Insere 10 registros iniciais
INSERT INTO usuarios (nome) VALUES
    ('Ana Silva'),
    ('Carlos Oliveira'),
    ('Mariana Santos'),
    ('Pedro Rocha'),
    ('Luiza Costa'),
    ('Rafael Lima'),
    ('Fernanda Alves'),
    ('Bruno Souza'),
    ('Juliana Pereira'),
    ('Lucas Gonçalves');