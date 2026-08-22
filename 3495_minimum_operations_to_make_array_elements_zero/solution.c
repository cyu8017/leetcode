// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

long long minOperations(int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    long long ans = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int l = queries[qi][0], r = queries[qi][1];
        long long sum = 0;
        for (int x = l; x <= r; x++) {
            int ops = 0, v = x;
            while (v > 0) { v /= 4; ops++; }
            sum += ops;
        }
        ans += (sum + 1) / 2;
    }
    return ans;
}
