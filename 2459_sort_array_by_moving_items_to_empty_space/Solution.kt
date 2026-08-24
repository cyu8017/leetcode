// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

import java.util.HashMap

class Solution {
    fun sortArray(nums: IntArray): Int {
            return minOf(SolveOne(nums, true), SolveOne(nums, false))
    }
    private fun solveOne(nums: IntArray, startZero: Boolean): Int {
            var n: Int = nums.size
            var arr: IntArray = nums.copyOf()
            var pos = HashMap()
            var i: Int = 0
    while (i < n) {
    pos.put(arr[i], i)
    i = i + 1
    }
            var ops: Int = 0
            while (true) {
                var empty: Int = pos.get(0)
                var should: Int = if (startZero) empty else (empty == n - 1 ? 0 : empty + 1)
                if (arr[empty] == should) {
                    var found: Int = -1
                    var i: Int = 0
    while (i < n) {
    
                        var want: Int = if (startZero) i else (i == n - 1 ? 0 : i + 1)
                        if (arr[i] != want) {
                            found = i
                            break
                        }
    
    i = i + 1
    }
                    if (found == -1) return ops
                    var v: Int = arr[found]
                    (arr[empty], arr[found]) = (arr[found], arr[empty])
                    pos.put(0, found)
                    pos.put(v, empty)
                    ops = ops + 1
                    continue
                }
                var j: Int = pos.get(should)
                var vv: Int = arr[j]
                (arr[empty], arr[j]) = (arr[j], arr[empty])
                pos.put(0, j)
                pos.put(vv, empty)
                ops = ops + 1
            }
    }
}
