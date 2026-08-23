// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

import java.util.TreeMap;

class Solution {
    public int maxTransactions(int[] transactions) {
        TreeMap<Integer, Integer> tm = new TreeMap<>();
        int ans = transactions.length;
        long s = 0;
        for (int x : transactions) {
            s += x;
            tm.merge(x, 1, Integer::sum);
            while (s < 0) {
                int y = tm.firstKey();
                s -= y;
                ans--;
                int c = tm.get(y);
                if (c == 1) tm.remove(y);
                else tm.put(y, c - 1);
            }
        }
        return ans;
    }
}
