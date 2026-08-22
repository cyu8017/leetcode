// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

int minimumOperations(int* nums, int numsSize) {
    int ops = 0, start = 0, n = numsSize;
    for (;;) {
        int seen[101] = {0}, dup = 0;
        for (int i = start; i < n; i++) {
            if (nums[i] >= 0 && nums[i] <= 100) {
                if (seen[nums[i]]) { dup = 1; break; }
                seen[nums[i]] = 1;
            } else {
                for (int j = start; j < i; j++) if (nums[j] == nums[i]) { dup = 1; break; }
                if (dup) break;
            }
        }
        if (!dup) return ops;
        if (n - start <= 3) return ops + 1;
        start += 3;
        ops++;
    }
}
