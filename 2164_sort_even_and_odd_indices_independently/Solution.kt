// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution {
    fun sortEvenOdd(nums: IntArray): IntArray {
        var even = mutableListOf()
        var odd = mutableListOf()
        for (i in 0 until nums.size) {
            if (i % 2 == 0) even.add(nums[i])
            else odd.add(nums[i])
        }
        even.sort()
        odd.sort(Collections.reverseOrder())
        var ei: Int = 0, oi = 0
        for (i in 0 until nums.size) {
            if (i % 2 == 0) nums[i] = even.get(ei++)
            else nums[i] = odd.get(oi++)
        }
        return nums
    }
}
