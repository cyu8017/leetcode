// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

public class Solution {
    public int[] PivotArray(int[] nums, int pivot) {
        var less = new List<int>();
        var eq = new List<int>();
        var greater = new List<int>();
        foreach (int x in nums) {
            if (x < pivot) less.Add(x);
            else if (x == pivot) eq.Add(x);
            else greater.Add(x);
        }
        less.AddRange(eq);
        less.AddRange(greater);
        return less.ToArray();
    }
}
