// LeetCode 0598 - Range Addition II
// https://leetcode.com/problems/range-addition-ii/

class Solution {
    func maxCount(_ m: Int, _ n: Int, _ ops: [[Int]]) -> Int {
        var m = m, n = n
        for op in ops {
            m = min(m, op[0])
            n = min(n, op[1])
        }
        return m * n
    }
}
