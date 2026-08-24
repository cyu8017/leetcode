// LeetCode 2504 - Concatenate The Name And The Profession
// https://leetcode.com/problems/concatenate-the-name-and-the-profession/

class Solution {
    companion object {
        const val QUERY = "SELECT person_id, CONCAT(name, \"(\", SUBSTRING(profession, 1, 1), \")\") AS name\n" +
            "FROM Person\n" +
            "ORDER BY person_id DESC"
    }
}
