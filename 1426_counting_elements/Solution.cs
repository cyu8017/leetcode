// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

using System.Collections.Generic;
public class Solution {
    public int CountElements(int[] arr) {
        var values = new HashSet<int>(arr);
        int ans = 0;
        foreach (int value in arr) if (values.Contains(value + 1)) ans++;
        return ans;
    }
}
