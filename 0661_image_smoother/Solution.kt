// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/


class Solution {
    fun imageSmoother(img: Array<IntArray>): Array<IntArray> {
        val m = img.size
        val n = img[0].size
        val result = Array(m) { IntArray(n) }
        for (i in 0 until m) {
            for (j in 0 until n) {
                var sum = 0
                var count = 0
                for (x in i - 1..i + 1) {
                    for (y in j - 1..j + 1) {
                        if (x in 0 until m && y in 0 until n) {
                            sum += img[x][y]
                            count++
                        }
                    }
                }
                result[i][j] = sum / count
            }
        }
        return result
    }
}
