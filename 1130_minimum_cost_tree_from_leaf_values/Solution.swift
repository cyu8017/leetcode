// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution {
    func mctFromLeafValues(_ arr: [Int]) -> Int {
        var stack = [Int.max]
        var ans = 0
        for x in arr {
            while stack.last! <= x {
                let mid = stack.removeLast()
                ans += mid * min(stack.last!, x)
            }
            stack.append(x)
        }
        while stack.count > 2 {
            ans += stack.removeLast() * stack.last!
        }
        return ans
    }
}
