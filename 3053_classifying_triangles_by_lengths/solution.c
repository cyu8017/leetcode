// LeetCode 3053 - Classifying Triangles by Lengths
// https://leetcode.com/problems/classifying-triangles-by-lengths/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    CASE\n"
    "        WHEN A + B <= C\n"
    "        OR A + C <= B\n"
    "        OR B + C <= A THEN 'Not A Triangle'\n"
    "        WHEN A = B\n"
    "        AND B = c THEN 'Equilateral'\n"
    "        WHEN (A = B) + (B = C) + (A = C) = 1 THEN 'Isosceles'\n"
    "        ELSE 'Scalene'\n"
    "    END AS triangle_type\n"
    "FROM Triangles;\n";
