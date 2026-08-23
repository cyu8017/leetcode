// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<String> findHighAccessEmployees(List<List<String>> accessTimes) {
        Map<String, List<Integer>> m = new HashMap<>();
        for (List<String> a : accessTimes) {
            String name = a.get(0), t = a.get(1);
            int hh = (t.charAt(0) - '0') * 10 + (t.charAt(1) - '0');
            int mm = (t.charAt(2) - '0') * 10 + (t.charAt(3) - '0');
            m.computeIfAbsent(name, k -> new ArrayList<>()).add(hh * 60 + mm);
        }
        List<String> ans = new ArrayList<>();
        for (Map.Entry<String, List<Integer>> e : m.entrySet()) {
            List<Integer> times = e.getValue();
            Collections.sort(times);
            for (int i = 0; i + 2 < times.size(); i++) {
                if (times.get(i + 2) - times.get(i) < 60) {
                    ans.add(e.getKey());
                    break;
                }
            }
        }
        Collections.sort(ans);
        return ans;
    }
}
