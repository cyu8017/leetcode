// LeetCode 1527 - Patients With A Condition
// https://leetcode.com/problems/patients-with-a-condition/

class Solution {
    companion object {
        const val QUERY = "SELECT patient_id, patient_name, conditions\n" +
            "FROM Patients\n" +
            "WHERE CONCAT(' ', conditions, ' ') LIKE '% DIAB1%'"
    }
}
