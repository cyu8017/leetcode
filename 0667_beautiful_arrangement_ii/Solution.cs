// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

public class Solution {
    public int[] ConstructArray(int n, int k) {
        var res = new System.Collections.Generic.List<int>();
        for (int i = 1; i <= n - k; ++i) res.Add(i);
        int left = n - k + 1, right = n;
        bool takeHigh = true;
        while (left <= right) {
            if (takeHigh) res.Add(right--);
            else res.Add(left++);
            takeHigh = !takeHigh;
        }
        return res.ToArray();
    }
}
