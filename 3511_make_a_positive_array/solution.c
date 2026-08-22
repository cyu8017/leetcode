// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

int makeArrayPositive(int* nums, int numsSize) {
    int ans = 0, l = -1;
    long long preMx = 0, s = 0;
    for (int r = 0; r < numsSize; r++) {
        s += nums[r];
        if (r - l > 2 && s <= preMx) {
            ans++;
            l = r;
            preMx = 0;
            s = 0;
        } else if (r - l >= 2) {
            long long cand = s - nums[r] - nums[r - 1];
            if (cand > preMx) preMx = cand;
        }
    }
    return ans;
}
