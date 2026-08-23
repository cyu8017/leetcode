// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

using System.Collections.Generic;

public class Solution {
    Dictionary<string, Dictionary<string, double>> BuildRateGraph(IList<IList<string>> pairs, double[] rates) {
        var g = new Dictionary<string, Dictionary<string, double>>();
        for (int i = 0; i < pairs.Count; i++) {
            string a = pairs[i][0], b = pairs[i][1];
            if (!g.ContainsKey(a)) g[a] = new Dictionary<string, double>();
            if (!g.ContainsKey(b)) g[b] = new Dictionary<string, double>();
            g[a][b] = rates[i];
            g[b][a] = 1.0 / rates[i];
        }
        return g;
    }

    Dictionary<string, double> Bellman(string start, IList<IList<string>> pairs, double[] rates) {
        var g = BuildRateGraph(pairs, rates);
        var dist = new Dictionary<string, double>();
        dist[start] = 1.0;
        for (int it = 0; it < 100; it++) {
            bool updated = false;
            foreach (var fromKv in g) {
                string from = fromKv.Key;
                if (!dist.ContainsKey(from) || dist[from] == 0) continue;
                foreach (var toKv in fromKv.Value) {
                    double nv = dist[from] * toKv.Value;
                    if (!dist.ContainsKey(toKv.Key) || nv > dist[toKv.Key]) {
                        dist[toKv.Key] = nv;
                        updated = true;
                    }
                }
            }
            if (!updated) break;
        }
        return dist;
    }

    public double MaxAmount(string initialCurrency, IList<IList<string>> pairs1, double[] rates1,
                           IList<IList<string>> pairs2, double[] rates2) {
        var amt1 = Bellman(initialCurrency, pairs1, rates1);
        double ans = 1.0;
        var g2 = BuildRateGraph(pairs2, rates2);
        foreach (var kv in amt1) {
            string c = kv.Key;
            double a = kv.Value;
            if (a <= 0) continue;
            var dist = new Dictionary<string, double>();
            dist[c] = a;
            bool updated = true;
            for (int it = 0; it < 100 && updated; it++) {
                updated = false;
                foreach (var fromKv in g2) {
                    string from = fromKv.Key;
                    if (!dist.ContainsKey(from) || dist[from] == 0) continue;
                    foreach (var toKv in fromKv.Value) {
                        double nv = dist[from] * toKv.Value;
                        if (!dist.ContainsKey(toKv.Key) || nv > dist[toKv.Key]) {
                            dist[toKv.Key] = nv;
                            updated = true;
                        }
                    }
                }
            }
            if (dist.ContainsKey(initialCurrency) && dist[initialCurrency] > ans)
                ans = dist[initialCurrency];
        }
        return ans;
    }
}
