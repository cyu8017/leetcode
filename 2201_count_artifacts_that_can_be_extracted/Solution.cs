// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

using System.Collections.Generic;

public class Solution {
    public int DigArtifacts(int n, int[][] artifacts, int[][] dig) {
        var dug = new HashSet<(int, int)>();
        foreach (var d in dig) dug.Add((d[0], d[1]));
        int ans = 0;
        foreach (var a in artifacts) {
            bool ok = true;
            for (int r = a[0]; r <= a[2]; r++)
                for (int c = a[1]; c <= a[3]; c++)
                    if (!dug.Contains((r, c))) ok = false;
            if (ok) ans++;
        }
        return ans;
    }
}
