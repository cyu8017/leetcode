// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

class Solution {
    private let MOD = 1_000_000_007

    private func group(_ p: [Int]) -> Int {
        if p[1] == 0 { return 0 }
        if p[0] > 0 { return 1 }
        return 2
    }

    func maxValue(_ nums1: [Int], _ nums0: [Int]) -> Int {
        let n = nums1.count
        var pairs = [[Int]]()
        var b = 0
        for i in 0..<n {
            pairs.append([nums1[i], nums0[i]])
            b += nums1[i] + nums0[i]
        }
        pairs.sort { a, c in
            let g1 = group(a), g2 = group(c)
            if g1 != g2 { return g1 < g2 }
            if g1 == 0 { return a[0] > c[0] }
            if g1 == 1 {
                if a[0] != c[0] { return a[0] > c[0] }
                return a[1] < c[1]
            }
            return a[1] < c[1]
        }
        var p = [Int](repeating: 0, count: max(b, 1))
        if b > 0 { p[0] = 1 }
        if b > 1 {
            for i in 1..<b { p[i] = 2 * p[i - 1] % MOD }
        }
        var ans = 0
        b -= 1
        for pr in pairs {
            var cnt1 = pr[0], cnt0 = pr[1]
            while cnt1 > 0 {
                ans = (ans + p[b]) % MOD
                b -= 1
                cnt1 -= 1
            }
            b -= cnt0
        }
        return ans
    }
}
