// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

class Solution {
    func resultGrid(_ image: [[Int]], _ threshold: Int) -> [[Int]] {
        let n = image.count, m = image[0].count
        var ans = Array(repeating: Array(repeating: 0, count: m), count: n)
        var ct = Array(repeating: Array(repeating: 0, count: m), count: n)
        var i = 0
        while i + 2 < n {
            var j = 0
            while j + 2 < m {
                var region = true
                for k in 0..<3 {
                    for l in 0..<2 {
                        if abs(image[i + k][j + l] - image[i + k][j + l + 1]) > threshold { region = false }
                    }
                }
                for k in 0..<2 {
                    for l in 0..<3 {
                        if abs(image[i + k][j + l] - image[i + k + 1][j + l]) > threshold { region = false }
                    }
                }
                if region {
                    var tot = 0
                    for k in 0..<3 {
                        for l in 0..<3 { tot += image[i + k][j + l] }
                    }
                    for k in 0..<3 {
                        for l in 0..<3 {
                            ct[i + k][j + l] += 1
                            ans[i + k][j + l] += tot / 9
                        }
                    }
                }
                j += 1
            }
            i += 1
        }
        for i in 0..<n {
            for j in 0..<m {
                if ct[i][j] == 0 { ans[i][j] = image[i][j] }
                else { ans[i][j] /= ct[i][j] }
            }
        }
        return ans
    }
}
