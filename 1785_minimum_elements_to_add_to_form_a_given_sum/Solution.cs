// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

public class Solution {
    public int MinElements(int[] nums, int limit, int goal) {
        long sum = 0;
        foreach (int num in nums) {
            sum += num;
        }
        long diff = Math.Abs(sum - goal);
        return (int)((diff + limit - 1) / limit);
    }
}
