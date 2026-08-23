// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

using System;
using System.Collections.Generic;

public class Solution {
    public long MakeSimilar(int[] nums, int[] target) {
        Array.Sort(nums);
        Array.Sort(target);
        var oddN = new List<int>();
        var evenN = new List<int>();
        var oddT = new List<int>();
        var evenT = new List<int>();
        foreach (int x in nums) {
            if (x % 2 == 0) evenN.Add(x);
            else oddN.Add(x);
        }
        foreach (int x in target) {
            if (x % 2 == 0) evenT.Add(x);
            else oddT.Add(x);
        }
        long ans = 0;
        for (int i = 0; i < oddN.Count; i++) {
            int diff = oddN[i] - oddT[i];
            if (diff > 0) ans += diff / 2;
        }
        for (int i = 0; i < evenN.Count; i++) {
            int diff = evenN[i] - evenT[i];
            if (diff > 0) ans += diff / 2;
        }
        return ans;
    }
}
