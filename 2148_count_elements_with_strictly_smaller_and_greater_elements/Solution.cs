// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

public class Solution {
    public int CountElements(int[] nums) {
        int mn = nums.Min(), mx = nums.Max();
        int ans = 0;
        foreach (int x in nums) if (x > mn && x < mx) ans++;
        return ans;
    }
}
