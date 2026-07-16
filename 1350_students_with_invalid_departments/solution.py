# LeetCode 1350 - Students With Invalid Departments

QUERY = """
SELECT s.id, s.name
FROM Students s
LEFT JOIN Departments d ON d.id = s.department_id
WHERE d.id IS NULL
"""
