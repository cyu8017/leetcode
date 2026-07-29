// LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

int minNumberOperations(int* target, int targetSize) {
    int ans = target[0];
    for (int i = 1; i < targetSize; i++) {
        if (target[i] > target[i - 1]) ans += target[i] - target[i - 1];
    }
    return ans;
}
