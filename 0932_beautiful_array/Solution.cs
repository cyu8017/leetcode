// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

using System.Collections.Generic;

public class Solution {
    public int[] BeautifulArray(int n) {
        if (n == 1) return new[] { 1 };
        var left = BeautifulArray((n + 1) / 2);
        var right = BeautifulArray(n / 2);
        var ans = new List<int>();
        foreach (int x in left) ans.Add(2 * x - 1);
        foreach (int x in right) ans.Add(2 * x);
        return ans.ToArray();
    }
}
