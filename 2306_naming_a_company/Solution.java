// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public long distinctNames(String[] ideas) {
        @SuppressWarnings("unchecked")
        Set<String>[] groups = new HashSet[26];
        for (int i = 0; i < 26; i++) groups[i] = new HashSet<>();
        for (String idea : ideas) groups[idea.charAt(0) - 'a'].add(idea.substring(1));
        long ans = 0;
        for (int i = 0; i < 26; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                int overlap = 0;
                for (String s : groups[i]) if (groups[j].contains(s)) overlap++;
                ans += (long) (groups[i].size() - overlap) * (groups[j].size() - overlap) * 2;
            }
        }
        return ans;
    }
}
