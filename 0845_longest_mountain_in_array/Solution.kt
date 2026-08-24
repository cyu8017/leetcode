// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

class Solution {
    fun longestMountain(arr: IntArray): Int {
        var n = arr.size
        var ans = 0
        var i = 0
        while (i < n) {
            var j = i
            if (j + 1 < n && arr[j] < arr[j + 1]) {
                while (j + 1 < n && arr[j] < arr[j + 1]) j++
                if (j + 1 < n && arr[j] > arr[j + 1]) {
                    while (j + 1 < n && arr[j] > arr[j + 1]) j++
                    ans = maxOf(ans, j - i + 1)
                    i = j
                    continue
                }
            }
            i++
        }
        return ans
    }
}
