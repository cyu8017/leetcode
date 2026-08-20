// LeetCode 1954 - Minimum Garden Perimeter to Collect Enough Apples
// https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

class Solution {
    func minimumPerimeter(_ neededApples: Int) -> Int {
        var lo = 1, hi = 100_000
        while lo < hi {
            let mid = (lo + hi) / 2
            let apples = 2 * mid * (mid + 1) * (2 * mid + 1)
            if apples >= neededApples { hi = mid } else { lo = mid + 1 }
        }
        return 8 * lo
    }
}
