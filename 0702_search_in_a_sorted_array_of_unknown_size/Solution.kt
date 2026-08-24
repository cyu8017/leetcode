// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

class ArrayReader {
    private val secret: IntArray? = null
    constructor(secret: IntArray) { this.secret = secret }
    fun get(index: Int): Int {
        if (index < 0 || index >= secret.size) return 2147483647
        return secret[index]
    }
}

class Solution {
    fun search(secret: IntArray, target: Int): Int {
        return search(ArrayReader(secret), target)
    }

    fun search(reader: ArrayReader, target: Int): Int {
        var right = 1
        while (reader[right] < target) right  shl = 1
        var left = right  shr  1
        while (left <= right) {
            var mid = left + (right - left) / 2
            var value = reader[mid]
            if (value == target) return mid
            if (value > target) right = mid - 1
            else left = mid + 1
        }
        return -1
    }
}
