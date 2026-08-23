// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxSubstrings(String word) {
        int ans = 0;
        var first = new HashMap<Character, Integer>();
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!first.containsKey(c)) first.put(c, i);
            else if (i - first.get(c) + 1 >= 4) {
                ans++;
                first.clear();
            }
        }
        return ans;
    }
}
