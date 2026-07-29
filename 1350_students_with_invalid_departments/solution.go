// LeetCode 1350 - Students With Invalid Departments
// https://leetcode.com/problems/students-with-invalid-departments/

const QUERY = `
SELECT s.id, s.name
FROM Students s
LEFT JOIN Departments d ON d.id = s.department_id
WHERE d.id IS NULL
`
