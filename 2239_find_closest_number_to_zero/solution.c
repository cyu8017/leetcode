// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

static int abs_i(int x) { return x < 0 ? -x : x; }

int findClosestNumber(int* nums, int numsSize) {
    int ans = nums[0];
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (abs_i(x) < abs_i(ans) || (abs_i(x) == abs_i(ans) && x > ans)) {
            ans = x;
        }
    }
    return ans;
}
