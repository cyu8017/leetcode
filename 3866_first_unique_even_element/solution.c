// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

int firstUniqueEven(int* nums, int numsSize) {
    int cnt[101] = {0};
    for (int i = 0; i < numsSize; i++) cnt[nums[i]]++;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0 && cnt[nums[i]] == 1) return nums[i];
    }
    return -1;
}
