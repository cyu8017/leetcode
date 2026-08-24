// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

class Solution {
    func minSubarraySort(_ nums: [Int], _ k: Int) -> [Int] {
        let inf = 1 << 30
        let n = nums.count
        var ans = [Int]()
        for i in 0...(n - k) { ans.append(f(nums, i, i + k - 1, inf)) }
        return ans
    }

    func f(_ nums: [Int], _ i: Int, _ j: Int, _ inf: Int) -> Int {
        var mi = inf, mx = -inf, l = -1, r = -1
        for p in i...j {
            if nums[p] < mx { r = p } else { mx = nums[p] }
            let q = j - p + i
            if nums[q] > mi { l = q } else { mi = nums[q] }
        }
        if r == -1 { return 0 }
        return r - l + 1
    }
}
