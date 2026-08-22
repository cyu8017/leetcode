// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

int maximumSum(int* arr, int arrSize) {
    int keep = arr[0];
    int del = arr[0];
    int ans = arr[0];
    for (int i = 1; i < arrSize; i++) {
        int x = arr[i];
        del = keep > del + x ? keep : del + x;
        keep = keep + x > x ? keep + x : x;
        if (keep > ans) ans = keep;
        if (del > ans) ans = del;
    }
    return ans;
}
