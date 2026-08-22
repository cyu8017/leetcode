// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

int minElement(int* nums, int numsSize) {
    int ans = 1000000000;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i], s = 0;
        while (x > 0) { s += x % 10; x /= 10; }
        if (s < ans) ans = s;
    }
    return ans;
}
