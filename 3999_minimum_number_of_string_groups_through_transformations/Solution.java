// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private static int leastRotation(String s) {
        int n = s.length();
        int i = 0, j = 1, k = 0;
        while (i < n && j < n && k < n) {
            char a = s.charAt((i + k) % n);
            char b = s.charAt((j + k) % n);
            if (a == b) ++k;
            else {
                if (a > b) i += k + 1;
                else j += k + 1;
                if (i == j) ++j;
                k = 0;
            }
        }
        return i < j ? i : j;
    }

    private static String canonicalRotate(String s) {
        int n = s.length();
        if (n <= 1) return s;
        int r = leastRotation(s);
        if (r == 0) return s;
        return s.substring(r) + s.substring(0, r);
    }

    public int minimumGroups(String[] words) {
        List<String> keys = new ArrayList<>();
        for (String w : words) {
            int n = w.length();
            StringBuilder even = new StringBuilder(), odd = new StringBuilder();
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0) even.append(w.charAt(i));
                else odd.append(w.charAt(i));
            }
            keys.add(canonicalRotate(even.toString()) + "#" + canonicalRotate(odd.toString()));
        }
        Collections.sort(keys);
        int groups = 0;
        for (int i = 0; i < keys.size(); i++) {
            if (i == 0 || !keys.get(i).equals(keys.get(i - 1))) ++groups;
        }
        return groups;
    }
}
