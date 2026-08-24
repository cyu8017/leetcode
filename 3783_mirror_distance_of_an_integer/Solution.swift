// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution {
    func mirrorDistance(_ n: Int) -> Int {
        return abs(n - reverse(n))
    }

    private func reverse(_ x: Int) -> Int {
        var x = x, y = 0
        while x > 0 {
            y = y * 10 + x % 10
            x /= 10
        }
        return y
    }
}
