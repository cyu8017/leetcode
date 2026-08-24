// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

class Solution {
    fun compose(functions: List<(Int) -> Int>): (Int) -> Int {
        return { x0 ->
            var x = x0
            for (i in functions.size - 1 downTo 0) x = functions[i](x)
            x
        }
    }
}
