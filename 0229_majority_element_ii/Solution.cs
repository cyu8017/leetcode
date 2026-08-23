// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

using System.Collections.Generic;

public class Solution {
    public IList<int> MajorityElement(int[] nums) {
        int? candidate1 = null;
        int? candidate2 = null;
        int count1 = 0;
        int count2 = 0;

        foreach (int num in nums) {
            if (candidate1.HasValue && num == candidate1.Value) {
                count1++;
            } else if (candidate2.HasValue && num == candidate2.Value) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        count1 = 0;
        count2 = 0;
        foreach (int num in nums) {
            if (candidate1.HasValue && num == candidate1.Value) {
                count1++;
            } else if (candidate2.HasValue && num == candidate2.Value) {
                count2++;
            }
        }

        int threshold = nums.Length / 3;
        var result = new List<int>();
        if (count1 > threshold) {
            result.Add(candidate1!.Value);
        }
        if (candidate2.HasValue && candidate2 != candidate1 && count2 > threshold) {
            result.Add(candidate2.Value);
        }
        return result;
    }
}
