// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

class Solution {
    fun resultGrid(image: Array<IntArray>, threshold: Int): Array<IntArray> {
        val n = image.size
        val m = image[0].size
        val ans = Array(n) { IntArray(m) }
        val ct = Array(n) { IntArray(m) }
        var i = 0
        while (i + 2 < n) {
            var j = 0
            while (j + 2 < m) {
                var region = true
                for (k in 0 until 3) {
                    for (l in 0 until 2) {
                        region = region && kotlin.math.abs(image[i + k][j + l] - image[i + k][j + l + 1]) <= threshold
                    }
                }
                for (k in 0 until 2) {
                    for (l in 0 until 3) {
                        region = region && kotlin.math.abs(image[i + k][j + l] - image[i + k + 1][j + l]) <= threshold
                    }
                }
                if (region) {
                    var tot = 0
                    for (k in 0 until 3) {
                        for (l in 0 until 3) tot += image[i + k][j + l]
                    }
                    for (k in 0 until 3) {
                        for (l in 0 until 3) {
                            ct[i + k][j + l]++
                            ans[i + k][j + l] += tot / 9
                        }
                    }
                }
                j++
            }
            i++
        }
        for (ii in 0 until n) {
            for (jj in 0 until m) {
                if (ct[ii][jj] == 0) ans[ii][jj] = image[ii][jj]
                else ans[ii][jj] /= ct[ii][jj]
            }
        }
        return ans
    }
}
