// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

class Solution {
    func compose(_ functions: [(Int) -> Int]) -> (Int) -> Int {
        return { x0 in
            var x = x0
            for i in stride(from: functions.count - 1, through: 0, by: -1) {
                x = functions[i](x)
            }
            return x
        }
    }
}
