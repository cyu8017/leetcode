// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

class Solution {
    fun largestEvenSum(nums: IntArray, k: Int): Long {
        val arr = nums.sortedDescending()
        var sum = 0L
        for (i in 0 until k) sum += arr[i]
        if (sum % 2L == 0L) return sum
        var ans = -1L
        var oddIn = -1
        var evenIn = -1
        var oddOut = -1
        var evenOut = -1
        for (i in k - 1 downTo 0) {
            if (arr[i] % 2 != 0 && oddIn == -1) oddIn = i
            if (arr[i] % 2 == 0 && evenIn == -1) evenIn = i
        }
        for (i in k until arr.size) {
            if (arr[i] % 2 != 0 && oddOut == -1) oddOut = i
            if (arr[i] % 2 == 0 && evenOut == -1) evenOut = i
        }
        if (oddIn != -1 && evenOut != -1) ans = maxOf(ans, sum - arr[oddIn] + arr[evenOut])
        if (evenIn != -1 && oddOut != -1) ans = maxOf(ans, sum - arr[evenIn] + arr[oddOut])
        return ans
    }
}
