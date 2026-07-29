// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

class Solution {
    func clumsy(_ n: Int) -> Int {
        var stack = [n]
        var n = n - 1
        var op = 0
        while n > 0 {
            if op % 4 == 0 {
                stack.append(stack.removeLast() * n)
            } else if op % 4 == 1 {
                stack.append(stack.removeLast() / n)
            } else if op % 4 == 2 {
                stack.append(n)
            } else {
                stack.append(-n)
            }
            n -= 1
            op += 1
        }
        return stack.reduce(0, +)
    }
}
