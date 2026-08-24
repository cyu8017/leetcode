// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

class Solution {
    func closestFair(_ n: Int) -> Int {
        var x = n
        while true {
            let s = Array(String(x))
            if s.count % 2 != 0 {
                var p = 1
                for _ in 0..<s.count { p *= 10 }
                return closestFair(p)
            }
            var even = 0, odd = 0
            for c in s {
                if (Int(String(c))! % 2) == 0 { even += 1 }
                else { odd += 1 }
            }
            if even == odd { return x }
            x += 1
        }
    }
}
