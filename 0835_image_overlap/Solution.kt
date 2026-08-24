// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

class Solution {
    fun largestOverlap(img1: Array<IntArray>, img2: Array<IntArray>): Int {
        var n = img1.size
        var ones1 = ArrayList<IntArray>()
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (img1[i][j] == 1) ones1.add(intArrayOf(i, j))
                if (img2[i][j] == 1) ones2.add(intArrayOf(i, j))
            }
        }
        if (ones1.isEmpty() || ones2.isEmpty()) return 0
        var shifts = HashMap<Long, Int>()
        var best = 0
        for (a in ones1) {
            for (b in ones2) {
                var key = ((a[0] - b[0] + n)  shl  16) | (a[1] - b[1] + n)
                best = maxOf(best, shifts.merge(key, 1, Integer::sum))
            }
        }
        return best
    }
}
