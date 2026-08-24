// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

class Solution {
    func reverseSubarrays(_ nums: [Int], _ k: Int) -> [Int] {
        var nums = nums
        let n = nums.count
        let m = n / k
        var i = 0
        while i < n {
            var lo = i, hi = i + m - 1
            while lo < hi {
                nums.swapAt(lo, hi)
                lo += 1
                hi -= 1
            }
            i += m
        }
        return nums
    }
}
