// LeetCode 1137 - N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

class Solution {
    func tribonacci(_ n: Int) -> Int {
        if n == 0 { return 0 }
        if n <= 2 { return 1 }
        var a = 0, b = 1, c = 1
        for _ in 3...n {
            let next = a + b + c
            a = b; b = c; c = next
        }
        return c
    }
}
