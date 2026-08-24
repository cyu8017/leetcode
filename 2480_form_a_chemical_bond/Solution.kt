// LeetCode 2480 - Form A Chemical Bond
// https://leetcode.com/problems/form-a-chemical-bond/

class Solution {
    companion object {
        const val QUERY = "SELECT a.symbol AS metal, b.symbol AS nonmetal\n" +
            "FROM\n" +
            "    Elements AS a,\n" +
            "    Elements AS b\n" +
            "WHERE a.type = 'Metal' AND b.type = 'Nonmetal'"
    }
}
