// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

using System.Collections.Generic;

public class Solution {
    string SprintfNum(int x) {
        if (x == 0) return "0";
        var b = new System.Text.StringBuilder();
        while (x > 0) {
            b.Insert(0, (char)('0' + x % 10));
            x /= 10;
        }
        return b.ToString();
    }

    bool AlmostEqual(int a, int b) {
        string sa = SprintfNum(a), sb = SprintfNum(b);
        while (sa.Length < sb.Length) sa = "0" + sa;
        while (sb.Length < sa.Length) sb = "0" + sb;
        var diff = new List<int>();
        for (int i = 0; i < sa.Length; i++) {
            if (sa[i] != sb[i]) diff.Add(i);
        }
        if (diff.Count == 0) return true;
        if (diff.Count != 2) return false;
        int i0 = diff[0], j = diff[1];
        return sa[i0] == sb[j] && sa[j] == sb[i0];
    }

    public int CountPairs(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.Length; i++)
            for (int j = i + 1; j < nums.Length; j++)
                if (AlmostEqual(nums[i], nums[j])) ans++;
        return ans;
    }
}
