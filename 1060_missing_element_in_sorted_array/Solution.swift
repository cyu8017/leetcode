// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution {
    func missingElement(_ nums: [Int], _ k: Int) -> Int {
        func missing(_ i: Int) -> Int {
            return nums[i] - nums[0] - i
        }
        let n = nums.count
        if k > missing(n - 1) {
            return nums[n - 1] + k - missing(n - 1)
        }
        var lo = 0
        var hi = n - 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if missing(mid) < k {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return nums[lo - 1] + k - missing(lo - 1)
    }
}
