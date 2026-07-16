// LeetCode 0031 - Next Permutation
// https://leetcode.com/problems/next-permutation/

static void swap_int(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void nextPermutation(int* nums, int numsSize) {
    int i = numsSize - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    if (i >= 0) {
        int j = numsSize - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        swap_int(&nums[i], &nums[j]);
    }

    int left = i + 1;
    int right = numsSize - 1;
    while (left < right) {
        swap_int(&nums[left], &nums[right]);
        left++;
        right--;
    }
}
