// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

int minCostToEqualizeArray(int* nums, int numsSize, int cost1, int cost2) {
    const int mod = 1000000007;
    int minNum = nums[0], maxNum = nums[0];
    long long sum = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < minNum) minNum = nums[i];
        if (nums[i] > maxNum) maxNum = nums[i];
        sum += nums[i];
    }
    if ((long long)cost1 * 2 <= cost2 || numsSize < 3) {
        long long totalGap = (long long)maxNum * numsSize - sum;
        return (int)((long long)cost1 * totalGap % mod);
    }
    long long ans = (1LL << 62);
    for (int target = maxNum; target < 2 * maxNum; target++) {
        int maxGap = target - minNum;
        long long totalGap = (long long)target * numsSize - sum;
        long long pairs = totalGap / 2;
        long long alt = totalGap - maxGap;
        if (alt < pairs) pairs = alt;
        long long cost = (long long)cost1 * (totalGap - 2 * pairs) + (long long)cost2 * pairs;
        if (cost < ans) ans = cost;
    }
    return (int)(ans % mod);
}
