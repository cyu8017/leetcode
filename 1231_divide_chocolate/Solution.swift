// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

class Solution {
    func maximizeSweetness(_ sweetness: [Int], _ k: Int) -> Int {
        var lo = 1, hi = sweetness.reduce(0, +) / (k + 1)
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            var cur = 0, cuts = 0
            for s in sweetness {
                cur += s
                if cur >= mid {
                    cuts += 1
                    cur = 0
                }
            }
            if cuts >= k + 1 { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }
}
