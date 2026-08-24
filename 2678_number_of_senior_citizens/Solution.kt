// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

class Solution {
    fun countSeniors(details: Array<String>): Int {
        var ans = 0
        for (d in details) {
            val age = (d[11] - '0') * 10 + (d[12] - '0')
            if (age > 60) ans++
        }
        return ans
    }
}
