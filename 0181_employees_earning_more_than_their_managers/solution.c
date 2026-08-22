// LeetCode 0181 - Employees Earning More Than Their Managers
// https://leetcode.com/problems/employees-earning-more-than-their-managers/

const char* QUERY =
    "\n"
    "SELECT e.name AS Employee\n"
    "FROM Employee e\n"
    "JOIN Employee m ON e.managerId = m.id\n"
    "WHERE e.salary > m.salary\n";