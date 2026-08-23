// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int longestBalanced(String s) {
        int cnt0 = 0;
        for (char c : s.toCharArray()) if (c == '0') cnt0++;
        int cnt1 = s.length() - cnt0;
        Map<Integer, List<Integer>> pos = new HashMap<>();
        pos.put(0, new ArrayList<>(List.of(-1)));
        int ans = 0, pre = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') pre++;
            else pre--;
            pos.computeIfAbsent(pre, k -> new ArrayList<>()).add(i);
            ans = Math.max(ans, i - pos.get(pre).get(0));
            if (pos.containsKey(pre - 2)) {
                List<Integer> p = pos.get(pre - 2);
                if ((i - p.get(0) - 2) / 2 < cnt0) ans = Math.max(ans, i - p.get(0));
                else if (p.size() > 1) ans = Math.max(ans, i - p.get(1));
            }
            if (pos.containsKey(pre + 2)) {
                List<Integer> p = pos.get(pre + 2);
                if ((i - p.get(0) - 2) / 2 < cnt1) ans = Math.max(ans, i - p.get(0));
                else if (p.size() > 1) ans = Math.max(ans, i - p.get(1));
            }
        }
        return ans;
    }
}
