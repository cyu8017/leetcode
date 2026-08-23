// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

import java.util.*;

class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> counts = new HashMap<>();
        for (String item : cpdomains) {
            int space = item.indexOf(' ');
            int count = Integer.parseInt(item.substring(0, space));
            String domain = item.substring(space + 1);
            while (true) {
                counts.merge(domain, count, Integer::sum);
                int dot = domain.indexOf('.');
                if (dot < 0) break;
                domain = domain.substring(dot + 1);
            }
        }
        List<String> ans = new ArrayList<>();
        for (Map.Entry<String, Integer> e : counts.entrySet()) {
            ans.add(e.getValue() + " " + e.getKey());
        }
        return ans;
    }
}
