// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

class Solution {
    fun kthCharacter(k: Long, operations: IntArray): Char {
        var shift = 0
        var ops = ArrayList<Int>()
        for (op in operations) { ops.add(op) }
        while (!ops.isEmpty()) {
            var op = ops.remove(ops.size - 1)
            var half = 1L  shl  ops.size
            if (k > half) {
                k -= half
                if (op == 1) shift++
            }
        }
        return (char) ('a' + shift % 26)
    }
}
