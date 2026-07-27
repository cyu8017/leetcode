// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

class Solution {
    func kthSmallestPath(_ destination: [Int], _ k: Int) -> String {
        var v = destination[0], h = destination[1]
        var k = k
        var ans = ""
        while h + v > 0 {
            if h > 0 {
                let count = comb(h + v - 1, v)
                if k <= count {
                    ans.append("H")
                    h -= 1
                    continue
                }
                k -= count
            }
            ans.append("V")
            v -= 1
        }
        return ans
    }

    private func comb(_ n: Int, _ k: Int) -> Int {
        if k < 0 || k > n { return 0 }
        var k = min(k, n - k)
        var res = 1
        if k == 0 { return 1 }
        for i in 1...k {
            res = res * (n - k + i) / i
        }
        return res
    }
}
