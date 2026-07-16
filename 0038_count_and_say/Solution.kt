// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

class Solution {
    fun countAndSay(n: Int): String {
        var term = "1"

        for (i in 1 until n) {
            val nextTerm = StringBuilder()
            var index = 0
            while (index < term.length) {
                var count = 1
                while (index + count < term.length && term[index + count] == term[index]) {
                    count++
                }
                nextTerm.append(count)
                nextTerm.append(term[index])
                index += count
            }
            term = nextTerm.toString()
        }

        return term
    }
}
