// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

class Solution {
    fun makeTheIntegerZero(num1: Int, num2: Int): Int {
        for (k in 1 ..60) {
            var rem = num1 - 1L * k * num2
            if (rem < k) continue
            if (BitOperations.PopCount((ulong)rem) <= k) return k
        }
        return -1
    }
}
