-- Active: 1706528093603@@127.0.0.1@3306@laplateforme
INSERT INTO etudiants (nom,prenom,age,email) VALUES 
('Dupuis','Martin',18,'martin.dupuis@laplateforme.io');

SELECT * FROM etudiants
WHERE nom = 'Dupuis';