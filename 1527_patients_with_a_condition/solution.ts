// LeetCode 1527 - Patients With A Condition
// https://leetcode.com/problems/patients-with-a-condition/

export const QUERY = `SELECT patient_id, patient_name, conditions
FROM Patients
WHERE CONCAT(' ', conditions, ' ') LIKE '% DIAB1%'`;
