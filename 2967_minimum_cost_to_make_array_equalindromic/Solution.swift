// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

class Solution {
    func minimumCost(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        let median = nums[n / 2]
        var candidates = [makePal(median)]
        let s = String(median)
        let halfLen = (s.count + 1) / 2
        let half = Int(s.prefix(halfLen))!
        for d in -2...2 {
            let h = half + d
            if h <= 0 { continue }
            let hs = String(h)
            let pal: String
            if s.count % 2 == 0 {
                pal = hs + String(hs.reversed())
            } else {
                let prefix = String(hs.dropLast())
                pal = hs + String(prefix.reversed())
            }
            if let p = Int(pal) { candidates.append(p) }
        }
        candidates.append(contentsOf: [1, 9, 11, 99, 101])
        var ans = Int.max / 4
        for p in candidates where p > 0 {
            ans = min(ans, cost(nums, p))
        }
        return ans
    }

    private func makePal(_ x: Int) -> Int {
        var ch = Array(String(x))
        var i = 0, j = ch.count - 1
        while i < j {
            ch[j] = ch[i]
            i += 1
            j -= 1
        }
        return Int(String(ch))!
    }

    private func cost(_ nums: [Int], _ p: Int) -> Int {
        var c = 0
        for v in nums { c += abs(v - p) }
        return c
    }
}
