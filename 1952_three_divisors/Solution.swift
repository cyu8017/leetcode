// LeetCode 1952 - Three Divisors
// https://leetcode.com/problems/three-divisors/

class Solution {
    func isThree(_ n: Int) -> Bool {
        let root = Int(Double(n).squareRoot())
        if root * root != n || root < 2 { return false }
        var i = 2
        while i * i <= root {
            if root % i == 0 { return false }
            i += 1
        }
        return true
    }
}
