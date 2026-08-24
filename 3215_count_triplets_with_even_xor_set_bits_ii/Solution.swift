// LeetCode 3215 - Count Triplets with Even XOR Set Bits II
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

class Solution {
    func tripletCount(_ a: [Int], _ b: [Int], _ c: [Int]) -> Int {
        var cnt1 = [0, 0], cnt2 = [0, 0], cnt3 = [0, 0]
        for x in a { cnt1[x.nonzeroBitCount % 2] += 1 }
        for x in b { cnt2[x.nonzeroBitCount % 2] += 1 }
        for x in c { cnt3[x.nonzeroBitCount % 2] += 1 }
        var ans = 0
        for i in 0..<2 {
            for j in 0..<2 {
                for k in 0..<2 where (i + j + k) % 2 == 0 {
                    ans += cnt1[i] * cnt2[j] * cnt3[k]
                }
            }
        }
        return ans
    }
}
