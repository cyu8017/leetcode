// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

class Solution {
    fun checkStrings(s1: String, s2: String): Boolean {
        val even1 = IntArray(26)
        val odd1 = IntArray(26)
        val even2 = IntArray(26)
        val odd2 = IntArray(26)
        for (i in s1.indices) {
            if (i % 2 == 0) {
                even1[s1[i] - 'a']++
                even2[s2[i] - 'a']++
            } else {
                odd1[s1[i] - 'a']++
                odd2[s2[i] - 'a']++
            }
        }
        return even1.contentEquals(even2) && odd1.contentEquals(odd2)
    }
}
