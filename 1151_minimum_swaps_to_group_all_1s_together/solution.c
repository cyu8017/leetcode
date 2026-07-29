// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

int minSwaps(int* data, int dataSize) {
    int ones = 0;
    for (int i = 0; i < dataSize; i++) ones += data[i];
    if (ones <= 1) return 0;
    int cur = 0;
    for (int i = 0; i < ones; i++) cur += data[i];
    int best = cur;
    for (int i = ones; i < dataSize; i++) {
        cur += data[i] - data[i - ones];
        if (cur > best) best = cur;
    }
    return ones - best;
}
