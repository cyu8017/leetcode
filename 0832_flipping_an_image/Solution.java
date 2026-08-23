// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for (int[] row : image) {
            for (int i = 0, j = row.length - 1; i <= j; i++, j--) {
                int a = 1 - row[i], b = 1 - row[j];
                row[i] = b;
                row[j] = a;
            }
        }
        return image;
    }
}
