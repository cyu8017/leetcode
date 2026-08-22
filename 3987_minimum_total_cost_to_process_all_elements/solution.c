// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

int minimumCost(int* nums, int numsSize, int k) {
    const long long mod = 1000000007LL;
    long long cnt = 0;
    long long cur = k;
    for (int i = 0; i < numsSize; i++) {
        long long x = nums[i];
        long long diff = x - cur;
        if (diff > 0) {
            long long m = (diff + k - 1) / k;
            cur += m * k;
            cnt += m;
        }
        cur -= x;
    }
    cnt %= mod;
    return (int)((cnt + 1) * cnt / 2 % mod);
}
