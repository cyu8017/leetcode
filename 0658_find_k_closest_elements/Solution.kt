// LeetCode 0658 - Find K Closest Elements
// https://leetcode.com/problems/find-k-closest-elements/


class Solution {
    fun findClosestElements(arr: IntArray, k: Int, x: Int): List<Int> {
        var left = 0
        var right = arr.size - k
        while (left < right) {
            val mid = (left + right) / 2
            if (x - arr[mid] > arr[mid + k] - x) left = mid + 1 else right = mid
        }
        return arr.slice(left until left + k)
    }
}
