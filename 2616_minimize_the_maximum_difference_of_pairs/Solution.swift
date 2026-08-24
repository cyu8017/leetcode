// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

class Solution {
    func minimizeMax(_ nums: [Int], _ p: Int) -> Int {
        let nums = nums.sorted()
        func ok(_ d: Int) -> Bool {
            var cnt = 0, i = 0
            while i + 1 < nums.count {
                if nums[i + 1] - nums[i] <= d {
                    cnt += 1
                    i += 2
                } else {
                    i += 1
                }
            }
            return cnt >= p
        }
        var lo = 0, hi = nums[nums.count - 1] - nums[0]
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
