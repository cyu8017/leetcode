// LeetCode 1375 - Number of Times Binary String Is Prefix-Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

int numTimesAllBlue(int* flips, int flipsSize) {
    int ans = 0, mx = 0;
    for (int i = 0; i < flipsSize; i++) {
        if (flips[i] > mx) mx = flips[i];
        if (mx == i + 1) ans++;
    }
    return ans;
}
