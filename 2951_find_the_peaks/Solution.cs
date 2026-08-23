// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

using System.Collections.Generic;

public class Solution {
    public IList<int> FindPeaks(int[] mountain) {
        var ans = new List<int>();
        for (int i = 1; i + 1 < mountain.Length; i++)
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1])
                ans.Add(i);
        return ans;
    }
}
