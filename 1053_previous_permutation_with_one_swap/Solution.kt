// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

class Solution {
    fun prevPermOpt1(arr: IntArray): IntArray {
        val n = arr.size
        var i = n - 2
        while (i >= 0 && arr[i] <= arr[i + 1]) i--
        if (i < 0) return arr
        var j = n - 1
        while (arr[j] >= arr[i] || arr[j] == arr[j - 1]) j--
        val tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        return arr
    }
}
