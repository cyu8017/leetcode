// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

import java.util.*;

class Solution {
    private Map<String, String> parent = new HashMap<>();

    private String find(String x) {
        parent.putIfAbsent(x, x);
        while (!parent.get(x).equals(x)) {
            parent.put(x, parent.get(parent.get(x)));
            x = parent.get(x);
        }
        return x;
    }

    private void unite(String a, String b) {
        parent.put(find(a), find(b));
    }

    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, String> emailName = new HashMap<>();
        parent.clear();
        for (List<String> account : accounts) {
            String name = account.get(0), first = account.get(1);
            for (int i = 1; i < account.size(); i++) {
                String email = account.get(i);
                parent.putIfAbsent(email, email);
                emailName.put(email, name);
                unite(first, email);
            }
        }
        Map<String, List<String>> groups = new HashMap<>();
        for (String email : parent.keySet()) {
            String root = find(email);
            groups.computeIfAbsent(root, k -> new ArrayList<>()).add(email);
        }
        List<List<String>> result = new ArrayList<>();
        for (List<String> emails : groups.values()) {
            Collections.sort(emails);
            List<String> row = new ArrayList<>();
            row.add(emailName.get(emails.get(0)));
            row.addAll(emails);
            result.add(row);
        }
        return result;
    }
}
