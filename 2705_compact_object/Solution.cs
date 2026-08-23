// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

// JS compactObject stand-in for int vectors: drop zeros
using System.Collections.Generic;

public class Solution {
    public int[] CompactObject(int[] obj) {
        var outList = new List<int>();
        foreach (int x in obj) if (x != 0) outList.Add(x);
        return outList.ToArray();
    }
}
