// LeetCode 3027 - Find the Number of Ways to Place People II
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

class Solution {
    func numberOfPairs(_ points: [[Int]]) -> Int {
        let points = points.sorted { a, b in
            a[0] != b[0] ? a[0] < b[0] : a[1] > b[1]
        }
        var ans = 0
        for i in 0..<points.count {
            let y1 = points[i][1]
            var maxY = Int.min
            for j in (i + 1)..<points.count {
                let y2 = points[j][1]
                if maxY < y2 && y2 <= y1 {
                    maxY = y2
                    ans += 1
                }
            }
        }
        return ans
    }
}
