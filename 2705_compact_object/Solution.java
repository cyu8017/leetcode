// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

import java.util.*;

// JS compactObject stand-in for int vectors: drop zeros
class Solution {
    public int[] compactObject(int[] obj) {
        List<Integer> out = new ArrayList<>();
        for (int x : obj) if (x != 0) out.add(x);
        int[] ans = new int[out.size()];
        for (int i = 0; i < out.size(); i++) ans[i] = out.get(i);
        return ans;
    }
}
