// LeetCode 0577 - Employee Bonus
// https://leetcode.com/problems/employee-bonus/

const char* QUERY =
    "\n"
    "SELECT e.name, b.bonus\n"
    "FROM Employee e\n"
    "LEFT JOIN Bonus b ON e.empId = b.empId\n"
    "WHERE b.bonus < 1000 OR b.bonus IS NULL\n";
