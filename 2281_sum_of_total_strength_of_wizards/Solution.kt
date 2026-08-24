// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

class Solution {

    fun totalStrength(strength: IntArray): Int {

            var mod = 1_000_000_007
            var n = strength.size
            var left = IntArray(n), right = IntArray(n)
            var stack = ArrayList<Int>()
            for (i in 0 until n) {
                while (!stack.isEmpty() && strength[stack[stack.size - 1]] >= strength[i])
                    stack.removeAt(stack.size - 1)
                left[i] = if (stack.isEmpty()) -1 else stack[stack.size - 1]
                stack.add(i)
            }
            stack.clear()
            for (i in n - 1 downTo 0) {
                while (!stack.isEmpty() && strength[stack[stack.size - 1]] > strength[i])
                    stack.removeAt(stack.size - 1)
                right[i] = if (stack.isEmpty()) n else stack[stack.size - 1]
                stack.add(i)
            }
            var pref = LongArray(n + 1), prefPref = LongArray(n + 2)
            for (i in 0 until n) { pref[i + 1] = (pref[i] + strength[i]) % mod }
            for (i in 0..n) { prefPref[i + 1] = (prefPref[i] + pref[i]) % mod }
            var ans = 0
            for (i in 0 until n) {
                var l = left[i] + 1; var r = right[i] - 1
                var leftSum = (prefPref[i + 1] - prefPref[l] + mod) % mod
                var rightSum = (prefPref[r + 2] - prefPref[i + 1] + mod) % mod
                var leftCnt = i - l + 1; var rightCnt = r - i + 1
                var contrib = (rightCnt * leftSum % mod - leftCnt * rightSum % mod + mod) % mod
                ans = (ans + contrib * strength[i] % mod) % mod
            }
            return ans.toInt()

    }

}
