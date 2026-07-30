// LeetCode 1389 - Create Target Array In The Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

using System.Collections.Generic;
public class Solution {
    public int[] CreateTargetArray(int[] nums, int[] index) {
        var outList = new List<int>();
        for (int i = 0; i < nums.Length; i++) outList.Insert(index[i], nums[i]);
        return outList.ToArray();
    }
}
