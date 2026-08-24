// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

class Solution {

    private fun gcd(a: Int, b: Int): Int {
        var _a = a
        var _b = b

            while (_b != 0) {
                var t = _a % _b
                _a = _b
                _b = t
            }
            return _a
    }


    fun replaceNonCoprimes(nums: IntArray): IntArray {

            var stack = ArrayList<Int>()
            for (x0 in nums) {
                var x = x0
                while (!stack.isEmpty()) {
                    var g = gcd(stack[stack.size - 1], x)
                    if (g == 1) break
                    x = stack[stack.size - 1] / g * x
                    stack.removeAt(stack.size - 1)
                }
                stack.add(x)
            }
            var ans = IntArray(stack.size)
            for (i in 0 until stack.size) { ans[i] = stack[i] }
            return ans

    }

}
