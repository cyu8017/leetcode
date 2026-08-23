// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

using System;
using System.Collections.Generic;

public class Solution {
    public int CountWays(IList<int> nums) {
        var arr = new List<int>(nums);
        arr.Sort();
        int n = arr.Count, ans = 0;
        if (arr[0] > 0) ans++;
        for (int i = 0; i < n; i++) {
            int selected = i + 1;
            if (selected > arr[i] && (i == n - 1 || selected < arr[i + 1])) ans++;
        }
        return ans;
    }
}
