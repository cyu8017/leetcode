// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> InvalidTransactions(string[] transactions) {
        var parsed = new List<(string name, int time, int amount, string city, string raw)>();
        foreach (var t in transactions) {
            var parts = t.Split(',');
            parsed.Add((parts[0], int.Parse(parts[1]), int.Parse(parts[2]), parts[3], t));
        }
        var invalid = new HashSet<string>();
        for (int i = 0; i < parsed.Count; i++) {
            var (name, time, amount, city, raw) = parsed[i];
            if (amount > 1000) invalid.Add(raw);
            for (int j = 0; j < parsed.Count; j++) {
                if (i == j) continue;
                var p2 = parsed[j];
                if (name == p2.name && city != p2.city && Math.Abs(time - p2.time) <= 60) {
                    invalid.Add(raw);
                    invalid.Add(p2.raw);
                }
            }
        }
        return new List<string>(invalid);
    }
}
