// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

class Solution {
    public int[][] imageSmoother(int[][] img) {
        int m = img.length;
        int n = img[0].length;
        int[][] out = new int[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int total = 0;
                int count = 0;
                for (int di = -1; di <= 1; ++di) {
                    for (int dj = -1; dj <= 1; ++dj) {
                        int ni = i + di;
                        int nj = j + dj;
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                            total += img[ni][nj];
                            ++count;
                        }
                    }
                }
                out[i][j] = total / count;
            }
        }
        return out;
    }
}
