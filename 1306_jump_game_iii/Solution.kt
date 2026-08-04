// LeetCode 1306 - Jump Game III
// https://leetcode.com/problems/jump-game-iii/

class Solution {
    fun canReach(arr: IntArray, start: Int): Boolean {
        val stack = ArrayDeque<Int>()
        val seen = mutableSetOf<Int>()
        stack.add(start)
        while (stack.isNotEmpty()) {
            val i = stack.removeLast()
            if (i in seen || i !in arr.indices) continue
            if (arr[i] == 0) return true
            seen.add(i)
            stack.add(i - arr[i])
            stack.add(i + arr[i])
        }
        return false
    }
}
