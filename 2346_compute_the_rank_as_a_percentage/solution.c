// LeetCode 2346 - Compute the Rank as a Percentage
// https://leetcode.com/problems/compute-the-rank-as-a-percentage/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    student_id,\n"
    "    department_id,\n"
    "    IFNULL(\n"
    "        ROUND(\n"
    "            (\n"
    "                RANK() OVER (\n"
    "                    PARTITION BY department_id\n"
    "                    ORDER BY mark DESC\n"
    "                ) - 1\n"
    "            ) * 100 / (COUNT(1) OVER (PARTITION BY department_id) - 1),\n"
    "            2\n"
    "        ),\n"
    "        0\n"
    "    ) AS percentage\n"
    "FROM Students\n";
