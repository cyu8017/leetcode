// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

import java.util.*;

class Solution {
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        int n = security.length;
        if (time == 0) {
            List<Integer> all = new ArrayList<>(n);
            for (int i = 0; i < n; i++) all.add(i);
            return all;
        }
        int[] left = new int[n], right = new int[n];
        for (int i = 1; i < n; i++) if (security[i] <= security[i - 1]) left[i] = left[i - 1] + 1;
        for (int i = n - 2; i >= 0; i--) if (security[i] <= security[i + 1]) right[i] = right[i + 1] + 1;
        List<Integer> ans = new ArrayList<>();
        for (int i = time; i < n - time; i++)
            if (left[i] >= time && right[i] >= time) ans.add(i);
        return ans;
    }
}
