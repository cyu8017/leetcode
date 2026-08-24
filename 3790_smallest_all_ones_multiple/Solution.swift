// LeetCode 3790 - Smallest All Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/

class Solution {
    func minAllOneMultiple(_ k: Int) -> Int {
        if (k & 1) == 0 { return -1 }
        var x = 1 % k
        var ans = 1
        for _ in 0..<k {
            x = (x * 10 + 1) % k
            ans += 1
            if x == 0 { return ans }
        }
        return -1
    }
}
