// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findPeaks(int[] mountain) {
        var ans = new ArrayList<Integer>();
        for (int i = 1; i + 1 < mountain.length; i++)
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1])
                ans.add(i);
        return ans;
    }
}
