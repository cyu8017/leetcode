// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

class Solution {
    func transformArray(_ arr: [Int]) -> [Int] {
        var cur = arr
        while true {
            var nxt = cur
            var changed = false
            for i in 1..<(cur.count - 1) {
                if cur[i] < cur[i - 1] && cur[i] < cur[i + 1] {
                    nxt[i] += 1; changed = true
                } else if cur[i] > cur[i - 1] && cur[i] > cur[i + 1] {
                    nxt[i] -= 1; changed = true
                }
            }
            cur = nxt
            if !changed { break }
        }
        return cur
    }
}
