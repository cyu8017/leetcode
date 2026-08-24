// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

import java.util.*;

class Solution {
    public int numSpecialEquivGroups(String[] words) {
        Set<String> groups = new HashSet<>();
        for (String w : words) {
            char[] even = new char[(w.length() + 1) / 2];
            char[] odd = new char[w.length() / 2];
            int ei = 0, oi = 0;
            for (int i = 0; i < w.length(); i++) {
                if (i % 2 == 0) even[ei++] = w.charAt(i);
                else odd[oi++] = w.charAt(i);
            }
            Arrays.sort(even);
            Arrays.sort(odd);
            groups.add(new String(even) + "|" + new String(odd));
        }
        return groups.size();
    }
}
