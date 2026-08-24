# LeetCode 1527 - Patients With A Condition
# https://leetcode.com/problems/patients-with-a-condition/

QUERY = <<~SQL
  SELECT patient_id, patient_name, conditions
  FROM Patients
  WHERE CONCAT(' ', conditions, ' ') LIKE '% DIAB1%'
SQL
