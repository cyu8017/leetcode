// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

class Solution {
    func minCost(_ basket1: [Int], _ basket2: [Int]) -> Int {
        var freq = [Int: Int]()
        var mn = Int.max
        for x in basket1 {
            freq[x, default: 0] += 1
            mn = min(mn, x)
        }
        for x in basket2 {
            freq[x, default: 0] -= 1
            mn = min(mn, x)
        }
        var extra = [Int]()
        for (k, v) in freq {
            if v % 2 != 0 { return -1 }
            for _ in 0..<(abs(v) / 2) { extra.append(k) }
        }
        extra.sort()
        var ans = 0
        for i in 0..<(extra.count / 2) {
            ans += min(extra[i], 2 * mn)
        }
        return ans
    }
}
