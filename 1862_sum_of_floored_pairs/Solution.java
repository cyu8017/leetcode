// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

class Solution {
    public int sumOfFlooredPairs(int[] nums) {
        int mod = 1_000_000_007;
        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }

        int[] count = new int[maxVal + 1];
        for (int num : nums) {
            count[num]++;
        }

        int[] prefix = new int[maxVal + 1];
        prefix[0] = count[0];
        for (int value = 1; value <= maxVal; value++) {
            prefix[value] = prefix[value - 1] + count[value];
        }

        long answer = 0;
        for (int divisor = 1; divisor <= maxVal; divisor++) {
            if (count[divisor] == 0) {
                continue;
            }
            int quotient = 1;
            while (quotient * divisor <= maxVal) {
                int low = quotient * divisor;
                int high = Math.min((quotient + 1) * divisor - 1, maxVal);
                int matches = prefix[high] - (low == 0 ? 0 : prefix[low - 1]);
                answer = (answer + (long) count[divisor] * matches * quotient) % mod;
                quotient++;
            }
        }

        return (int) answer;
    }
}
