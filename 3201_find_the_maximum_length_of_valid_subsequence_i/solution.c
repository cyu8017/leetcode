// LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

int maximumLength(int* nums, int numsSize) {
    int k = 2, f[2][2] = {{0}}, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i] % k;
        for (int j = 0; j < k; j++) {
            int y = (j - x + k) % k;
            f[x][y] = f[y][x] + 1;
            if (f[x][y] > ans) ans = f[x][y];
        }
    }
    return ans;
}
