// LeetCode 3262 - Find Overlapping Shifts
// https://leetcode.com/problems/find-overlapping-shifts/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    t1.employee_id,\n"
    "    COUNT(*) AS overlapping_shifts\n"
    "FROM\n"
    "    EmployeeShifts t1\n"
    "    JOIN EmployeeShifts t2\n"
    "        ON t1.employee_id = t2.employee_id\n"
    "        AND t1.start_time < t2.start_time\n"
    "        AND t1.end_time > t2.start_time\n"
    "GROUP BY 1\n"
    "HAVING overlapping_shifts > 0\n"
    "ORDER BY 1;\n";
