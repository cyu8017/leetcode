// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

class Solution {
    func minEnd(_ n: Int, _ x: Int) -> Int {
        var rem = n - 1
        var ans = x
        for i in 0..<31 {
            if ((x >> i) & 1) == 0 {
                ans |= (rem & 1) << i
                rem >>= 1
            }
        }
        ans |= rem << 31
        return ans
    }
}
