// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

int specialArray(int* nums, int numsSize) {
    for (int x = 0; x <= numsSize; x++) {
        int cnt = 0;
        for (int i = 0; i < numsSize; i++) if (nums[i] >= x) cnt++;
        if (cnt == x) return x;
    }
    return -1;
}
