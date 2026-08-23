// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

public class Solution {
    public bool IsMiddleElementUnique(int[] nums) {
        int mid = nums[nums.Length / 2];
        int cnt = 0;
        foreach (int x in nums) {
            if (x == mid) cnt++;
        }
        return cnt == 1;
    }
}
