// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

class Solution {
    func minimumIncompatibility(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let size = n / k
        let full = (1 << n) - 1
        var groups = [Int: Int]()
        for mask in 0..<(1 << n) {
            if mask.nonzeroBitCount != size { continue }
            var vals = [Int]()
            for i in 0..<n where (mask >> i) & 1 == 1 {
                vals.append(nums[i])
            }
            if Set(vals).count == size {
                groups[mask] = vals.max()! - vals.min()!
            }
        }
        var memo = [Int: Int]()
        let inf = 1_000_000_000
        func dp(_ mask: Int) -> Int {
            if mask == full { return 0 }
            if let v = memo[mask] { return v }
            var first = 0
            while (mask >> first) & 1 == 1 { first += 1 }
            var best = inf
            for (g, c) in groups {
                if ((g >> first) & 1) == 1 && (g & mask) == 0 {
                    best = min(best, c + dp(mask | g))
                }
            }
            memo[mask] = best
            return best
        }
        let ans = dp(0)
        return ans >= inf ? -1 : ans
    }
}
