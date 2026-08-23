// LeetCode 2504 - Concatenate the Name and the Profession
// https://leetcode.com/problems/concatenate-the-name-and-the-profession/

const char* QUERY = R"SQL(
SELECT person_id, CONCAT(name, "(", SUBSTRING(profession, 1, 1), ")") AS name
FROM Person
ORDER BY person_id DESC
)SQL";
