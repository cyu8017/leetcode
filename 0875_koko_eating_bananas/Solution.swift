// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

class Solution {
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        var lo = 1, hi = piles.max() ?? 1
        while lo < hi {
            let mid = (lo + hi) / 2
            var hours = 0
            for p in piles { hours += (p + mid - 1) / mid }
            if hours <= h { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }
}
