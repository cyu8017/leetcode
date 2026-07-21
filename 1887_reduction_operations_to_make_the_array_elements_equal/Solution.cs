// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

public class Solution {
    public int ReductionOperations(int[] nums) {
        Array.Sort(nums);
        int answer = 0;
        int rank = 0;
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] != nums[i - 1]) {
                rank++;
            }
            answer += rank;
        }
        return answer;
    }
}
