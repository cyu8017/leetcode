// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

class NumArray {
    private final int[] nums;
    private final int[] tree;

    public NumArray(int[] nums) {
        this.nums = nums.clone();
        this.tree = new int[nums.length + 1];
        for (int index = 0; index < nums.length; index++) {
            add(index + 1, nums[index]);
        }
    }

    public void update(int index, int val) {
        int delta = val - nums[index];
        nums[index] = val;
        add(index + 1, delta);
    }

    public int sumRange(int left, int right) {
        return prefix(right + 1) - prefix(left);
    }

    private void add(int index, int delta) {
        while (index <= nums.length) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    private int prefix(int index) {
        int total = 0;
        while (index > 0) {
            total += tree[index];
            index -= index & -index;
        }
        return total;
    }
}
