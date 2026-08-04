// LeetCode 1343 - Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution {
    fun numOfSubarrays(arr: IntArray, k: Int, threshold: Int): Int {
        var window = 0
        for (i in 0 until k) window += arr[i]
        var answer = if (window >= k * threshold) 1 else 0
        for (i in k until arr.size) {
            window += arr[i] - arr[i - k]
            if (window >= k * threshold) answer++
        }
        return answer
    }
}
