// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

public class Solution {
    public long MinArraySum(int[] nums) {
        int maximum = 0;
        bool[] present = new bool[100001];
        foreach (int value in nums) {
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
        foreach (int value in nums) answer += best[value];
        return answer;
    }
}
