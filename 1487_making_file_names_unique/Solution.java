// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

import java.util.*;

class Solution {
    public String[] getFolderNames(String[] names) {
        Map<String, Integer> used = new HashMap<>();
        String[] ans = new String[names.length];
        for (int i = 0; i < names.length; i++) {
            String name = names[i], candidate;
            if (!used.containsKey(name)) {
                candidate = name;
            } else {
                int k = used.get(name);
                while (used.containsKey(name + "(" + k + ")")) k++;
                candidate = name + "(" + k + ")";
                used.put(name, k + 1);
            }
            used.put(candidate, 1);
            ans[i] = candidate;
        }
        return ans;
    }
}
