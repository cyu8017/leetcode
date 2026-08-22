// LeetCode 1527 - Patients With a Condition
// https://leetcode.com/problems/patients-with-a-condition/

const char* QUERY =
    "\n"
    "SELECT patient_id, patient_name, conditions\n"
    "FROM Patients\n"
    "WHERE CONCAT(' ', conditions, ' ') LIKE '% DIAB1%'\n";
