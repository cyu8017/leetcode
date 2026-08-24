// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

class Solution {
    fun flipAndInvertImage(image: Array<IntArray>): Array<IntArray> {
        for (row in image) {
            var i = 0, j = row.size - 1
            while (i <= j) {
                var a = 1 - row[i]
                var b = 1 - row[j]
                row[i] = b
                row[j] = a
                i++, j--
            }
        }
        return image
    }
}
