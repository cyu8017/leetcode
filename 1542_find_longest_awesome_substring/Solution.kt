// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

class Solution {
    fun longestAwesome(s: String): Int {
        val first = HashMap<Int, Int>()
        first[0] = -1
        var mask = 0
        var answer = 0
        for (i in s.indices) {
            mask = mask xor (1 shl (s[i] - '0'))
            if (first.containsKey(mask)) {
                answer = maxOf(answer, i - first[mask]!!)
            } else {
                first[mask] = i
            }
            for (bit in 0 until 10) {
                val candidate = mask xor (1 shl bit)
                if (first.containsKey(candidate)) {
                    answer = maxOf(answer, i - first[candidate]!!)
                }
            }
        }
        return answer
    }
}
