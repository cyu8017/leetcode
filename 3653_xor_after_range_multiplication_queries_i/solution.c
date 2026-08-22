// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

int xorAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    const int mod = 1000000007;
    for (int qi = 0; qi < queriesSize; qi++) {
        int l = queries[qi][0], r = queries[qi][1], k = queries[qi][2], v = queries[qi][3];
        for (int idx = l; idx <= r; idx += k) nums[idx] = (int)((long long)nums[idx] * v % mod);
    }
    int ans = 0;
    for (int i = 0; i < numsSize; i++) ans ^= nums[i];
    return ans;
}
