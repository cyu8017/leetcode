// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

class Solution {
    func countPairs(_ coordinates: [[Int]], _ k: Int) -> Int {
        var freq: [Int: Int] = [:]
        var ans = 0
        for p in coordinates {
            let x = p[0], y = p[1]
            for a in 0...k {
                let b = k - a
                ans += freq[key(x ^ a, y ^ b), default: 0]
            }
            freq[key(x, y), default: 0] += 1
        }
        return ans
    }

    private func key(_ x: Int, _ y: Int) -> Int {
        return (x << 32) ^ (y & 0xffffffff)
    }
}
