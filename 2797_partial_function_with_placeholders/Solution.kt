// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/
// JS-only problem; Java stand-in with Integer.MIN_VALUE as placeholder.

import java.util.function.ToIntFunction

class Solution {
    fun partial(fn: ToIntFunction<IntArray>, args: IntArray): ToIntFunction<IntArray> {
        return ToIntFunction { rest ->
            val full = ArrayList<Int>()
            var ri = 0
            for (a in args) {
                if (a == Int.MIN_VALUE) {
                    if (ri < rest.size) full.add(rest[ri++])
                } else {
                    full.add(a)
                }
            }
            while (ri < rest.size) full.add(rest[ri++])
            val arr = IntArray(full.size)
            for (i in full.indices) arr[i] = full[i]
            fn.applyAsInt(arr)
        }
    }
}
