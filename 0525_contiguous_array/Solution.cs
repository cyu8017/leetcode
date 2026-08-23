// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

public class Solution {
    public int FindMaxLength(int[] nums) {
        Dictionary<int, int> counts = new() { [0] = -1 };
        int balance = 0;
        int best = 0;
        for (int index = 0; index < nums.Length; index++) {
            balance += nums[index] == 1 ? 1 : -1;
            if (counts.TryGetValue(balance, out int previous)) {
                best = Math.Max(best, index - previous);
            } else {
                counts[balance] = index;
            }
        }
        return best;
    }
}
