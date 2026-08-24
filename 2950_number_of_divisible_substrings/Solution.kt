// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

class Solution {
    fun countDivisibleSubstrings(word: String): Int {
        var vals = {1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9}
        var ans = 0
        var n = word.length
        for (i in 0 until n) {
            var sum = 0
            for (j in i until n) {
                sum += vals[word[j] - 'a']
                if (sum % (j - i + 1) == 0) ans++
            }
        }
        return ans
    }
}
