// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

import java.util.*;

class Solution {
    public int countTriples(int n) {
        Set<Integer> squares = new HashSet<>();
        for (int i = 1; i <= n; i++) squares.add(i * i);
        int ans = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                if (squares.contains(a * a + b * b)) ans++;
            }
        }
        return ans;
    }
}
