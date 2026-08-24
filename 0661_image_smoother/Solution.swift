// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

class Solution {
    func imageSmoother(_ img: [[Int]]) -> [[Int]] {
        let m = img.count, n = img[0].count
        var out = Array(repeating: Array(repeating: 0, count: n), count: m)
        for i in 0..<m {
            for j in 0..<n {
                var total = 0, count = 0
                for di in -1...1 {
                    for dj in -1...1 {
                        let ni = i + di, nj = j + dj
                        if ni >= 0 && ni < m && nj >= 0 && nj < n {
                            total += img[ni][nj]
                            count += 1
                        }
                    }
                }
                out[i][j] = total / count
            }
        }
        return out
    }
}
