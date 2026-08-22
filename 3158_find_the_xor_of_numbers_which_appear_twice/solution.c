// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

int duplicateNumbersXOR(int* nums, int numsSize) {
    int cnt[51] = {0}, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        cnt[nums[i]]++;
        if (cnt[nums[i]] == 2) ans ^= nums[i];
    }
    return ans;
}
