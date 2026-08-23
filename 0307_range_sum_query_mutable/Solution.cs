// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

public class NumArray {
    private readonly int[] nums;
    private readonly int[] tree;

    public NumArray(int[] nums) {
        this.nums = (int[])nums.Clone();
        tree = new int[nums.Length + 1];
        for (int index = 0; index < nums.Length; index++) {
            Add(index + 1, nums[index]);
        }
    }

    public void Update(int index, int val) {
        int delta = val - nums[index];
        nums[index] = val;
        Add(index + 1, delta);
    }

    public int SumRange(int left, int right) {
        return Prefix(right + 1) - Prefix(left);
    }

    private void Add(int index, int delta) {
        while (index <= nums.Length) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    private int Prefix(int index) {
        int total = 0;
        while (index > 0) {
            total += tree[index];
            index -= index & -index;
        }
        return total;
    }
}
