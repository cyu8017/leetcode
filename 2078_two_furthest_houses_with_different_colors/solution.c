// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

int maxDistance(int* colors, int colorsSize) {
    int n = colorsSize, ans = 0;
    for (int i = 0; i < n; i++) {
        if (colors[i] != colors[0] && i > ans) ans = i;
        if (colors[i] != colors[n - 1] && n - 1 - i > ans) ans = n - 1 - i;
    }
    return ans;
}
