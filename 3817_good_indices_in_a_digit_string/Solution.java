// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] goodIndices(String s) {
        var ans = new ArrayList<Integer>();
        for (int i = 0; i < s.length(); i++) {
            String t = String.valueOf(i);
            int k = t.length();
            if (i + 1 - k >= 0 && s.substring(i + 1 - k, k) == t) ans.add(i);
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
