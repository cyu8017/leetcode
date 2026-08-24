// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

class Solution {
    func maxGoodNumber(_ nums: [Int]) -> Int {
        func toBin(_ x: Int) -> String {
            if x == 0 { return "0" }
            var x = x
            var s = ""
            while x > 0 {
                s = String(x & 1) + s
                x >>= 1
            }
            return s
        }
        let bs = nums.map { toBin($0) }
        var idx = [0, 1, 2]
        var ans = 0
        func perm(_ i: Int) {
            if i == 3 {
                let s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]]
                var v = 0
                for c in s { v = v * 2 + Int(String(c))! }
                if v > ans { ans = v }
                return
            }
            for j in i..<3 {
                idx.swapAt(i, j)
                perm(i + 1)
                idx.swapAt(i, j)
            }
        }
        perm(0)
        return ans
    }
}
