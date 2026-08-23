// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

// JS ArrayWrapper stand-in
class ArrayWrapper {
    private final int[] nums;

    public ArrayWrapper(int[] nums) {
        this.nums = nums;
    }

    public int valueOf() {
        int s = 0;
        for (int x : nums) s += x;
        return s;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append('[');
        for (int i = 0; i < nums.length; i++) {
            if (i > 0) sb.append(',');
            sb.append(nums[i]);
        }
        sb.append(']');
        return sb.toString();
    }
}

class Solution {
    public ArrayWrapper arrayWrapperCreate(int[] nums) {
        return new ArrayWrapper(nums);
    }
}
