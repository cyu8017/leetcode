// LeetCode 0075 - Sort Colors
// https://leetcode.com/problems/sort-colors/

static void swap_int(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void sortColors(int* nums, int numsSize) {
    int low = 0;
    int mid = 0;
    int high = numsSize - 1;

    while (mid <= high) {
        if (nums[mid] == 0) {
            swap_int(&nums[low], &nums[mid]);
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
            swap_int(&nums[mid], &nums[high]);
            high--;
        }
    }
}
