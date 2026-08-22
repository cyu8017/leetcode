// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

int minimumDeletions(int* nums, int numsSize) {
    int n = numsSize, mi = 0, ma = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] < nums[mi]) mi = i;
        if (nums[i] > nums[ma]) ma = i;
    }
    if (mi > ma) { int t = mi; mi = ma; ma = t; }
    int a = ma + 1, b = n - mi, c = mi + 1 + n - ma;
    int ans = a;
    if (b < ans) ans = b;
    if (c < ans) ans = c;
    return ans;
}
