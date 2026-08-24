// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

class ArrayReader(private val arr: IntArray) {
    fun compareSub(l: Int, r: Int, x: Int, y: Int): Int {
        var a = 0L
        var b = 0L
        for (i in l..r) a += arr[i]
        for (i in x..y) b += arr[i]
        return a.compareTo(b)
    }

    fun length(): Int = arr.size
}

class Solution {
    fun getIndex(arr: IntArray): Int = getIndex(ArrayReader(arr))

    fun getIndex(reader: ArrayReader): Int {
        var left = 0
        var right = reader.length() - 1
        while (left < right) {
            val length = right - left + 1
            val half = length / 2
            val result = reader.compareSub(left, left + half - 1, right - half + 1, right)
            when {
                result == 0 -> return left + half
                result > 0 -> right = left + half - 1
                else -> left = right - half + 1
            }
        }
        return left
    }
}
