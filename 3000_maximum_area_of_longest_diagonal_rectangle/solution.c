// LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

int areaOfMaxDiagonal(int** dimensions, int dimensionsSize, int* dimensionsColSize) {
    (void)dimensionsColSize;
    int mx = 0, ans = 0;
    for (int i = 0; i < dimensionsSize; i++) {
        int l = dimensions[i][0], w = dimensions[i][1];
        int t = l * l + w * w;
        if (mx < t) {
            mx = t;
            ans = l * w;
        } else if (mx == t) {
            int area = l * w;
            if (area > ans) ans = area;
        }
    }
    return ans;
}
