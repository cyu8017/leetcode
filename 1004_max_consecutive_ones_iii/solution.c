// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

int longestOnes(int* nums, int numsSize, int k) {
    int left = 0, zeros = 0, ans = 0;
    for (int right = 0; right < numsSize; right++) {
        zeros += nums[right] == 0;
        while (zeros > k) {
            zeros -= nums[left] == 0;
            left++;
        }
        int len = right - left + 1;
        if (len > ans) ans = len;
    }
    return ans;
}
