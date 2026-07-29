// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

int maxTurbulenceSize(int* arr, int arrSize) {
    int ans = 1, cur = 1;
    for (int i = 1; i < arrSize; i++) {
        if (arr[i] == arr[i - 1]) cur = 1;
        else if (i == 1 || (long long)(arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0) cur++;
        else cur = 2;
        if (cur > ans) ans = cur;
    }
    return ans;
}
