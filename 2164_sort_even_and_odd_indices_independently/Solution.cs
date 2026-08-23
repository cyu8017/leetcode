// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

public class Solution {
    public int[] SortEvenOdd(int[] nums) {
        var even = new List<int>();
        var odd = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (i % 2 == 0) even.Add(nums[i]);
            else odd.Add(nums[i]);
        }
        even.Sort();
        odd.Sort((a, b) => b.CompareTo(a));
        int ei = 0, oi = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (i % 2 == 0) nums[i] = even[ei++];
            else nums[i] = odd[oi++];
        }
        return nums;
    }
}
