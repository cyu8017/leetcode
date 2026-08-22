// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

int maximumSum(int* nums, int numsSize) {
    int best[82];
    for (int i = 0; i < 82; i++) best[i] = 0;
    int ans = -1;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i], ds = 0, t = x;
        while (t > 0) { ds += t % 10; t /= 10; }
        if (best[ds] > 0) {
            if (best[ds] + x > ans) ans = best[ds] + x;
            if (x > best[ds]) best[ds] = x;
        } else best[ds] = x;
    }
    return ans;
}
