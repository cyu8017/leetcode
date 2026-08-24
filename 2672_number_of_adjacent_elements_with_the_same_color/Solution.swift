// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution {
    func colorTheArray(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var colors = Array(repeating: 0, count: n)
        var ans = Array(repeating: 0, count: queries.count)
        var same = 0
        for i in queries.indices {
            let idx = queries[i][0], color = queries[i][1]
            if colors[idx] != 0 {
                if idx > 0 && colors[idx] == colors[idx - 1] { same -= 1 }
                if idx + 1 < n && colors[idx] == colors[idx + 1] { same -= 1 }
            }
            colors[idx] = color
            if idx > 0 && colors[idx] == colors[idx - 1] { same += 1 }
            if idx + 1 < n && colors[idx] == colors[idx + 1] { same += 1 }
            ans[i] = same
        }
        return ans
    }
}
