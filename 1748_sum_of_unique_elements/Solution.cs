// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

public class Solution {
    public int SumOfUnique(int[] nums) {
        var counts = new Dictionary<int, int>();
        foreach (int value in nums) {
            counts[value] = counts.TryGetValue(value, out int count) ? count + 1 : 1;
        }
        int total = 0;
        foreach (var entry in counts) {
            if (entry.Value == 1) {
                total += entry.Key;
            }
        }
        return total;
    }
}
