// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

import java.util.*;

class Solution {
    public boolean reorderedPowerOf2(int n) {
        String target = sig(n);
        for (int i = 0; i < 31; i++) if (sig(1 << i).equals(target)) return true;
        return false;
    }

    private String sig(int x) {
        char[] s = Integer.toString(x).toCharArray();
        Arrays.sort(s);
        return new String(s);
    }
}
