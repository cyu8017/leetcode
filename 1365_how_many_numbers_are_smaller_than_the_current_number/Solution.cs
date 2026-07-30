// LeetCode 1365 - How Many Numbers Are Smaller Than The Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        var sorted = (int[])nums.Clone();
        System.Array.Sort(sorted);
        var answer = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++) {
            int lo = 0, hi = sorted.Length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (sorted[mid] < nums[i]) lo = mid + 1; else hi = mid;
            }
            answer[i] = lo;
        }
        return answer;
    }
}
