// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

class Solution {
    func flipAndInvertImage(_ image: [[Int]]) -> [[Int]] {
        var image = image
        for r in 0..<image.count {
            var i = 0, j = image[r].count - 1
            while i <= j {
                let a = 1 - image[r][i], b = 1 - image[r][j]
                image[r][i] = b
                image[r][j] = a
                i += 1
                j -= 1
            }
        }
        return image
    }
}
