// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

import java.util.*;

class Solution {
    private List<Integer> ans = new ArrayList<>();
    private int n, k;

    public int[] numsSameConsecDiff(int n, int k) {
        this.n = n;
        this.k = k;
        for (int start = 1; start <= 9; start++) dfs(start, 1);
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }

    private void dfs(int num, int length) {
        if (length == n) {
            ans.add(num);
            return;
        }
        int last = num % 10;
        Set<Integer> nexts = new HashSet<>();
        nexts.add(last + k);
        nexts.add(last - k);
        for (int nxt : nexts) {
            if (nxt >= 0 && nxt <= 9) dfs(num * 10 + nxt, length + 1);
        }
    }
}
