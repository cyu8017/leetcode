// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int uniqueEmailGroups(String[] emails) {
        Set<String> st = new HashSet<>();
        for (String email : emails) {
            int at = email.indexOf('@');
            String local = email.substring(0, at);
            String domain = email.substring(at + 1).toLowerCase();
            int plus = local.indexOf('+');
            if (plus >= 0) local = local.substring(0, plus);
            StringBuilder cleaned = new StringBuilder();
            for (char c : local.toCharArray()) if (c != '.') cleaned.append(Character.toLowerCase(c));
            st.add(cleaned.toString() + domain);
        }
        return st.size();
    }
}
