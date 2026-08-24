// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/
// JS generator stand-in returning factorial sequence.

class Solution {
    fun factorialGenerator(n: Int): MutableList<Int> {
        var ans = ArrayList<Int>()
        var cur = 1
        for (i in 1 ..n) {
            cur *= i
            ans.add(cur)
        }
        return ans
    }
}
