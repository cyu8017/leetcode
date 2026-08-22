// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

int countKDifference(int* nums, int numsSize, int k) {
    int freq[101] = {0};
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x - k >= 1 && x - k <= 100) ans += freq[x - k];
        if (x + k >= 1 && x + k <= 100) ans += freq[x + k];
        freq[x]++;
    }
    return ans;
}
