// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

class Solution {
    public long minArraySum(int[] nums) {
        int maximum = 0;
        boolean[] present = new boolean[100001];
        for (int value : nums) {
            present[value] = true;
            if (value > maximum) maximum = value;
        }
        int[] best = new int[maximum + 1];
        for (int divisor = 1; divisor <= maximum; divisor++) {
            if (!present[divisor]) continue;
            for (int multiple = divisor; multiple <= maximum; multiple += divisor) {
                if (best[multiple] == 0) best[multiple] = divisor;
            }
        }
        long answer = 0;
        for (int value : nums) answer += best[value];
        return answer;
    }
}
