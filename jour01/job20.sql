-- Active: 1706528093603@@127.0.0.1@3306@laplateforme
SELECT COUNT(*) AS nombre_etudiants_mineurs
FROM etudiants
WHERE age < 18;
