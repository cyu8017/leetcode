// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

class Solution {
    func factorialGenerator(_ n: Int) -> [Int] {
        var ans: [Int] = []
        var cur = 1
        if n >= 1 {
            for i in 1...n {
                cur *= i
                ans.append(cur)
            }
        }
        return ans
    }

    func factorialGen() -> () -> Int {
        var i = 0
        var cur = 1
        return {
            if i == 0 {
                i = 1
                return 1
            }
            cur *= i
            i += 1
            return cur
        }
    }
}
