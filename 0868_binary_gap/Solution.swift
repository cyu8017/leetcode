// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

class Solution {
    func binaryGap(_ n: Int) -> Int {
        var n = n, last = -1, ans = 0, bit = 0
        while n != 0 {
            if n & 1 == 1 {
                if last != -1 { ans = max(ans, bit - last) }
                last = bit
            }
            n >>= 1
            bit += 1
        }
        return ans
    }
}
