// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

class Solution {
    func uniqueXorTriplets(_ nums: [Int]) -> Int {
        var mx = 0
        for v in nums { mx = max(mx, v) }
        mx <<= 1
        var st = Array(repeating: false, count: mx)
        for a in nums {
            for b in nums { st[a ^ b] = true }
        }
        var s = Array(repeating: 0, count: mx)
        for ab in 0..<mx {
            if st[ab] {
                for c in nums { s[ab ^ c] = 1 }
            }
        }
        var ans = 0
        for v in s { ans += v }
        return ans
    }
}
