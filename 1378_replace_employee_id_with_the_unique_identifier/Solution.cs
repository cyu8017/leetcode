// LeetCode 1378 - Replace Employee ID With The Unique Identifier
// https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

public class Solution {
    public const string QUERY = @"
SELECT euni.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI euni ON e.id = euni.id
";
}
