// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

public class Solution {
    public int[] SortJumbled(int[] mapping, int[] nums) {
        int MapVal(int x) {
            if (x == 0) return mapping[0];
            var digits = new List<int>();
            while (x > 0) { digits.Add(x % 10); x /= 10; }
            int res = 0;
            for (int i = digits.Count - 1; i >= 0; i--)
                res = res * 10 + mapping[digits[i]];
            return res;
        }
        var arr = new (int mapped, int idx, int val)[nums.Length];
        for (int i = 0; i < nums.Length; i++)
            arr[i] = (MapVal(nums[i]), i, nums[i]);
        Array.Sort(arr);
        int[] ans = new int[nums.Length];
        for (int i = 0; i < arr.Length; i++) ans[i] = arr[i].val;
        return ans;
    }
}
