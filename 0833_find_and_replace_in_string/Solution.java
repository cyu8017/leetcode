// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

import java.util.*;

class Solution {
    public String findReplaceString(String s, int[] indices, String[] sources, String[] targets) {
        Map<Integer, int[]> replaceIdx = new HashMap<>();
        Map<Integer, String> replaceStr = new HashMap<>();
        for (int k = 0; k < indices.length; k++) {
            int i = indices[k];
            if (s.startsWith(sources[k], i)) {
                replaceIdx.put(i, new int[] {sources[k].length()});
                replaceStr.put(i, targets[k]);
            }
        }
        StringBuilder out = new StringBuilder();
        int i = 0, n = s.length();
        while (i < n) {
            if (replaceStr.containsKey(i)) {
                out.append(replaceStr.get(i));
                i += replaceIdx.get(i)[0];
            } else {
                out.append(s.charAt(i));
                i++;
            }
        }
        return out.toString();
    }
}
