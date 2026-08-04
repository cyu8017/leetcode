// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution {
    public int minSwaps(int[] data) {
        int ones = 0;
        for (int x : data) ones += x;
        if (ones <= 1) return 0;
        int cur = 0;
        for (int i = 0; i < ones; i++) cur += data[i];
        int best = cur;
        for (int i = ones; i < data.length; i++) {
            cur += data[i] - data[i - ones];
            best = Math.max(best, cur);
        }
        return ones - best;
    }
}
