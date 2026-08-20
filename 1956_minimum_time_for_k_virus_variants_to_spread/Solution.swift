// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

class Solution {
    func minDayskVariants(_ points: [[Int]], _ k: Int) -> Int {
        var ans = Int.max
        for x in 1...100 {
            for y in 1...100 {
                var dists = points.map { abs($0[0] - x) + abs($0[1] - y) }
                dists.sort()
                ans = min(ans, dists[k - 1])
            }
        }
        return ans
    }
}
