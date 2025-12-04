-- 3. Все оценки Alice Johnson
SELECT subject, grade 
FROM grades 
WHERE student_id = (SELECT id FROM students WHERE full_name = 'Alice Johnson');

-- 4. Средний балл по каждому студенту
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC;

-- 5. Студенты, родившиеся после 2004 года
SELECT full_name, birth_year 
FROM students 
WHERE birth_year > 2004;

-- 6. Средний балл по каждому предмету
SELECT subject, ROUND(AVG(grade), 2) AS average_grade
FROM grades
GROUP BY subject
ORDER BY average_grade DESC;

-- 7. Топ-3 студентов с самым высоким средним баллом
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 3;

-- 8. Студенты, у которых есть хотя бы одна оценка ниже 80
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name;