// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

// JS ArrayWrapper stand-in
using System.Text;

public class ArrayWrapper {
    int[] nums;
    public ArrayWrapper(int[] nums) { this.nums = nums; }
    public int ValueOf() {
        int s = 0;
        foreach (int x in nums) s += x;
        return s;
    }
    public override string ToString() {
        var sb = new StringBuilder();
        sb.Append('[');
        for (int i = 0; i < nums.Length; i++) {
            if (i > 0) sb.Append(',');
            sb.Append(nums[i]);
        }
        sb.Append(']');
        return sb.ToString();
    }
}

public class Solution {
    public ArrayWrapper ArrayWrapperCreate(int[] nums) => new ArrayWrapper(nums);
}
