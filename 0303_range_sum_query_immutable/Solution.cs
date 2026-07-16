// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

public class NumArray {
    private readonly int[] prefix;

    public NumArray(int[] nums) {
        prefix = new int[nums.Length + 1];
        for (int index = 0; index < nums.Length; index++) {
            prefix[index + 1] = prefix[index] + nums[index];
        }
    }

    public int SumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
}
