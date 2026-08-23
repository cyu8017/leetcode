// LeetCode 1527 - Patients With a Condition
// https://leetcode.com/problems/patients-with-a-condition/

class Solution {
    public static final String QUERY = """
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE CONCAT(' ', conditions, ' ') LIKE '% DIAB1%'
""";
}
