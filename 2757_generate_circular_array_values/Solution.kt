// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/
// JS generator stand-in.

import java.util.function.IntSupplier

class Solution {
    fun cyclicGenerator(arr: IntArray, startIndex: Int): IntSupplier {
        return object : IntSupplier {
            private var i = startIndex
            private val n = arr.size
            override fun getAsInt(): Int {
                val v = arr[i]
                i = (i + 1) % n
                return v
            }
        }
    }
}
