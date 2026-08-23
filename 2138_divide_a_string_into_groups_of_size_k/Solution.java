// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

import java.util.*;

class Solution {
    public String[] divideString(String s, int k, char fill) {
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < s.length(); i += k) {
            if (i + k <= s.length()) ans.add(s.substring(i, i + k));
            else {
                StringBuilder chunk = new StringBuilder(s.substring(i));
                while (chunk.length() < k) chunk.append(fill);
                ans.add(chunk.toString());
            }
        }
        return ans.toArray(new String[0]);
    }
}
