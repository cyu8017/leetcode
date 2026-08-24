// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution {
    fun maxDifference(s: String): Int {
        var freq = IntArray(26)
        for (c in s.toCharArray()) { freq[c - 'a']++ }
        var maxOdd = 0
        var minEven = 1000000000
        for (f in freq) {
            if (f == 0) continue
            if (f % 2 == 1) {
                if (f > maxOdd) maxOdd = f
            } else if (f < minEven) minEven = f
        }
        return maxOdd - minEven
    }
}
