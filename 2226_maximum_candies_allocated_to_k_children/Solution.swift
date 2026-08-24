// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution {
    func maximumCandies(_ candies: [Int], _ k: Int) -> Int {
        func can(_ mid: Int) -> Bool {
            if mid == 0 { return true }
            var cnt = 0
            for c in candies {
                cnt += c / mid
                if cnt >= k { return true }
            }
            return false
        }
        var lo = 0, hi = candies.max() ?? 0
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if can(mid) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }
}
