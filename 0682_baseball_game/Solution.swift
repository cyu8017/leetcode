// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

class Solution {
    func calPoints(_ operations: [String]) -> Int {
        var stack = [Int]()
        for op in operations {
            if op == "+" {
                stack.append(stack[stack.count - 1] + stack[stack.count - 2])
            } else if op == "D" {
                stack.append(stack.last! * 2)
            } else if op == "C" {
                stack.removeLast()
            } else {
                stack.append(Int(op)!)
            }
        }
        return stack.reduce(0, +)
    }
}
