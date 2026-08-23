// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

using System.Collections.Generic;

public class Solution {
    public int[] AddNegabinary(int[] arr1, int[] arr2) {
        int i = arr1.Length - 1, j = arr2.Length - 1, carry = 0;
        var ans = new List<int>();
        while (i >= 0 || j >= 0 || carry != 0) {
            int total = carry;
            if (i >= 0) {
                total += arr1[i--];
            }
            if (j >= 0) {
                total += arr2[j--];
            }
            ans.Add(total & 1);
            carry = -(total >> 1);
        }
        while (ans.Count > 1 && ans[ans.Count - 1] == 0) {
            ans.RemoveAt(ans.Count - 1);
        }
        ans.Reverse();
        return ans.ToArray();
    }
}
