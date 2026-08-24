// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

class Solution {
    private func bitLen(_ x: Int) -> Int {
        if x == 0 { return 0 }
        var x = x, n = 0
        while x > 0 { n += 1; x >>= 1 }
        return n
    }

    private func lis(_ arr: [Int]) -> Int {
        var g = [Int]()
        for x in arr {
            var lo = 0, hi = g.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if g[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            if lo == g.count { g.append(x) }
            else { g[lo] = x }
        }
        return g.count
    }

    func longestSubsequence(_ nums: [Int]) -> Int {
        var ans = 0, mx = 0
        for x in nums { mx = max(mx, x) }
        let m = bitLen(mx)
        for i in 0..<m {
            var arr = [Int]()
            for x in nums where ((x >> i) & 1) != 0 { arr.append(x) }
            ans = max(ans, lis(arr))
        }
        return ans
    }
}
