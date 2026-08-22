// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

long long numberOfSubsequences(int* nums, int numsSize) {
    int n = numsSize; long long ans = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 2; j < n; j++)
            for (int k = j + 2; k < n; k++)
                for (int l = k + 2; l < n; l++)
                    if ((long long)nums[i] * nums[k] == (long long)nums[j] * nums[l]) ans++;
    return ans;
}
