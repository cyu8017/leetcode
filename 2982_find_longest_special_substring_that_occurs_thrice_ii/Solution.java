// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int maximumLength(String s) {
        @SuppressWarnings("unchecked")
        List<Integer>[] groups = new ArrayList[26];
        for (int c = 0; c < 26; c++) groups[c] = new ArrayList<>();
        int n = s.length();
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s.charAt(j) == s.charAt(i)) j++;
            groups[s.charAt(i) - 'a'].add(j - i);
            i = j;
        }
        int ans = -1;
        for (int c = 0; c < 26; c++) {
            List<Integer> arr = groups[c];
            if (arr.isEmpty()) continue;
            arr.sort((a, b) -> Integer.compare(b, a));
            for (int L = arr.get(0); L >= 1; L--) {
                int cnt = 0;
                for (int g : arr) {
                    if (g >= L) cnt += g - L + 1;
                }
                if (cnt >= 3) {
                    if (L > ans) ans = L;
                    break;
                }
            }
        }
        return ans;
    }
}
