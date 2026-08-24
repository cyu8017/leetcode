// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

class Solution {
    fun countPermutations(complexity: IntArray): Int {
        val mod = 1000000007
        var ans = 1
        for (i in 1 until complexity.size) {
            if (complexity[i] <= complexity[0]) return 0
            ans = ans * i % mod
        }
        return ans
    }
}
