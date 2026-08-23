// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

using System.Collections.Generic;

public class Solution {
    public int[] ResultArray(int[] nums) {
        var arr1 = new List<int> { nums[0] };
        var arr2 = new List<int> { nums[1] };
        for (int i = 2; i < nums.Length; i++) {
            if (arr1[arr1.Count - 1] > arr2[arr2.Count - 1]) arr1.Add(nums[i]);
            else arr2.Add(nums[i]);
        }
        arr1.AddRange(arr2);
        return arr1.ToArray();
    }
}
