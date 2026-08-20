// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

class Solution {
    func maxSideLength(_ mat: [[Int]], _ threshold: Int) -> Int {
        let m = mat.count, n = mat[0].count
        var pref = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: m + 1)
        for i in 1...m {
            for j in 1...n {
                pref[i][j] = mat[i - 1][j - 1] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1]
            }
        }
        func sum(_ r1: Int, _ c1: Int, _ r2: Int, _ c2: Int) -> Int {
            pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1]
        }
        var ans = 0
        for i in 1...m {
            for j in 1...n {
                var lo = 1, hi = min(i, j)
                while lo <= hi {
                    let mid = (lo + hi) / 2
                    if sum(i - mid + 1, j - mid + 1, i, j) <= threshold {
                        ans = max(ans, mid)
                        lo = mid + 1
                    } else {
                        hi = mid - 1
                    }
                }
            }
        }
        return ans
    }
}
