// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

import java.util.*;

class Solution {
    private String num;
    private List<Integer> path;

    public List<Integer> splitIntoFibonacci(String num) {
        this.num = num;
        path = new ArrayList<>();
        dfs(0);
        return path;
    }

    private boolean dfs(int start) {
        int n = num.length();
        if (start == n) return path.size() >= 3;
        long val = 0;
        for (int end = start; end < n; end++) {
            if (num.charAt(start) == '0' && end > start) break;
            val = val * 10 + (num.charAt(end) - '0');
            if (val > Integer.MAX_VALUE) break;
            if (path.size() >= 2) {
                long total = (long) path.get(path.size() - 1) + path.get(path.size() - 2);
                if (val < total) continue;
                if (val > total) break;
            }
            path.add((int) val);
            if (dfs(end + 1)) return true;
            path.remove(path.size() - 1);
        }
        return false;
    }
}
