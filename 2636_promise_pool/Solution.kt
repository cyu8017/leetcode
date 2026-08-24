// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

class Solution {
    fun promisePool(functions: List<() -> Int>, n: Int): IntArray {
        val ans = IntArray(functions.size)
        for (i in functions.indices) ans[i] = functions[i]()
        return ans
    }
}
