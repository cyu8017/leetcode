// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

class Solution {
    func mergeAdjacent(_ nums: [Int]) -> [Int] {
        var stk = [Int]()
        for x in nums {
            stk.append(x)
            while stk.count > 1 && stk[stk.count - 1] == stk[stk.count - 2] {
                let a = stk.removeLast()
                let b = stk.removeLast()
                stk.append(a + b)
            }
        }
        return stk
    }
}
