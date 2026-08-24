// LeetCode 3932 - Count K-th Roots in a Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/


class Solution {
    func countKthRoots(_ l: Int, _ r: Int, _ k: Int) -> Int {
        if k == 1 { return r - l + 1 }
        var ans = 0
        var x = 0
        while true {
            var y = 1
            var tooBig = false
            for _ in 0..<k {
                if x != 0 && y > r / x {
                    tooBig = true
                    break
                }
                y *= x
                if y > r { break }
            }
            if tooBig || y > r { break }
            if l <= y && y <= r { ans += 1 }
            x += 1
        }
        return ans
    }
}
