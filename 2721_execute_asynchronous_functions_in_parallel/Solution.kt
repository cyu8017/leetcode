// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

class Solution {
    fun promiseAll(functions: List<() -> Int>): IntArray {
        val out = IntArray(functions.size)
        for (i in functions.indices) out[i] = functions[i]()
        return out
    }
}
