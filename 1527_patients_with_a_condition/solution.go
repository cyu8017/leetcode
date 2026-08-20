// LeetCode 1527 - Patients With a Condition
// https://leetcode.com/problems/patients-with-a-condition/

const QUERY = `
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE CONCAT(' ', conditions, ' ') LIKE '% DIAB1%'
`
