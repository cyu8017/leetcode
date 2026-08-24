// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

class Solution {
    func minCapability(_ nums: [Int], _ k: Int) -> Int {
        var lo = nums.min()!, hi = nums.max()!
        func ok(_ cap: Int) -> Bool {
            var cnt = 0, i = 0
            while i < nums.count {
                if nums[i] <= cap {
                    cnt += 1
                    i += 2
                } else {
                    i += 1
                }
            }
            return cnt >= k
        }
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
