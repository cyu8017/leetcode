// LeetCode 1346 - Check If N and Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution {
    fun checkIfExist(arr: IntArray): Boolean {
        val seen = HashSet<Int>()
        for (value in arr) {
            if (2 * value in seen || (value % 2 == 0 && value / 2 in seen)) return true
            seen.add(value)
        }
        return false
    }
}
