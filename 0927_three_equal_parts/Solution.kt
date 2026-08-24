// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

class Solution {
    fun threeEqualParts(arr: IntArray): IntArray {
        val ones = mutableListOf<Int>()
        for (i in arr.indices) if (arr[i] != 0) ones.add(i)
        val n = ones.size
        if (n % 3 != 0) return intArrayOf(-1, -1)
        if (n == 0) return intArrayOf(0, arr.size - 1)
        val third = n / 3
        val length = ones[ones.size - 1] - ones[2 * third] + 1
        val a = ones[0]
        val b = ones[third]
        val c = ones[2 * third]
        if (a + length > arr.size || b + length > arr.size || c + length > arr.size)
            return intArrayOf(-1, -1)
        for (i in 0 until length) {
            if (arr[a + i] != arr[b + i] || arr[a + i] != arr[c + i]) return intArrayOf(-1, -1)
        }
        return intArrayOf(a + length - 1, b + length)
    }
}
