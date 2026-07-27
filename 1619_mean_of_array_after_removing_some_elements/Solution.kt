// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution {
    fun trimMean(arr: IntArray): Double {
        arr.sort()
        val k = arr.size / 20
        var sum = 0.0
        for (i in k until arr.size - k) sum += arr[i]
        return sum / (arr.size - 2 * k)
    }
}
