// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int shortestMatchingSubstring(String s, String p) {
        List<String> parts = new ArrayList<>();
        StringBuilder cur = new StringBuilder();
        for (char c : p.toCharArray()) {
            if (c == '*') {
                parts.add(cur.toString());
                cur.setLength(0);
            } else cur.append(c);
        }
        parts.add(cur.toString());
        while (parts.size() < 3) parts.add("");
        String a = parts.get(0), b = parts.get(1), c = parts.get(2);
        int n = s.length();
        List<Integer> posA = findAll(s, a), posB = findAll(s, b), posC = findAll(s, c);
        int ans = n + 1;
        for (int ia : posA) {
            int endA = ia + a.length();
            int bi = sortSearch(posB, endA);
            for (; bi < posB.size(); bi++) {
                int endB = posB.get(bi) + b.length();
                int ci = sortSearch(posC, endB);
                if (ci < posC.size()) {
                    int length = posC.get(ci) + c.length() - ia;
                    if (length < ans) ans = length;
                }
                break;
            }
        }
        return ans == n + 1 ? -1 : ans;
    }

    private List<Integer> findAll(String s, String sub) {
        List<Integer> res = new ArrayList<>();
        int n = s.length();
        if (sub.isEmpty()) {
            for (int i = 0; i <= n; i++) res.add(i);
            return res;
        }
        for (int i = 0; i + sub.length() <= n; i++) {
            if (s.regionMatches(i, sub, 0, sub.length())) res.add(i);
        }
        return res;
    }

    private int sortSearch(List<Integer> arr, int x) {
        int i = Collections.binarySearch(arr, x);
        return i >= 0 ? i : -i - 1;
    }
}
