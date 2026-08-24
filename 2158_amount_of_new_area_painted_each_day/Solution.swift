// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

class Solution {
    func amountPainted(_ paint: [[Int]]) -> [Int] {
        var ans = [Int](repeating: 0, count: paint.count)
        var line = [Int](repeating: 0, count: 50001)
        for i in 0..<paint.count {
            let start = paint[i][0], end = paint[i][1]
            var j = start
            while j < end {
                if line[j] == 0 {
                    ans[i] += 1
                    line[j] = end
                    j += 1
                } else {
                    let next = line[j]
                    line[j] = max(end, next)
                    j = next
                }
            }
        }
        return ans
    }
}
