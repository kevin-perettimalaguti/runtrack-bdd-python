-- Active: 1706528093603@@127.0.0.1@3306@laplateforme
SELECT COUNT(*) AS etudiant_entre_18_25
FROM etudiants
WHERE age BETWEEN 18 AND 25;