// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> stringSequence(String target) {
        List<String> ans = new ArrayList<>();
        StringBuilder cur = new StringBuilder();
        for (char ch : target.toCharArray()) {
            cur.append('a');
            ans.add(cur.toString());
            while (cur.charAt(cur.length() - 1) != ch) {
                cur.setCharAt(cur.length() - 1, (char) (cur.charAt(cur.length() - 1) + 1));
                ans.add(cur.toString());
            }
        }
        return ans;
    }
}
