// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

import java.util.*;

class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> normalized = new HashSet<>();
        for (String email : emails) {
            int at = email.indexOf('@');
            String local = email.substring(0, at);
            String domain = email.substring(at);
            int plus = local.indexOf('+');
            if (plus >= 0) local = local.substring(0, plus);
            StringBuilder cleaned = new StringBuilder();
            for (char c : local.toCharArray()) if (c != '.') cleaned.append(c);
            normalized.add(cleaned.toString() + domain);
        }
        return normalized.size();
    }
}
