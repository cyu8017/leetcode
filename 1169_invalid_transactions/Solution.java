// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

import java.util.*;

class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        int n = transactions.length;
        String[] name = new String[n];
        int[] time = new int[n], amount = new int[n];
        String[] city = new String[n];
        for (int i = 0; i < n; i++) {
            String[] p = transactions[i].split(",");
            name[i] = p[0]; time[i] = Integer.parseInt(p[1]);
            amount[i] = Integer.parseInt(p[2]); city[i] = p[3];
        }
        Set<String> invalid = new LinkedHashSet<>();
        for (int i = 0; i < n; i++) {
            if (amount[i] > 1000) invalid.add(transactions[i]);
            for (int j = 0; j < n; j++) {
                if (i != j && name[i].equals(name[j]) && !city[i].equals(city[j]) && Math.abs(time[i] - time[j]) <= 60) {
                    invalid.add(transactions[i]);
                    invalid.add(transactions[j]);
                }
            }
        }
        return new ArrayList<>(invalid);
    }
}
