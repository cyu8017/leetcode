// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private Map<String, Map<String, Double>> buildRateGraph(List<List<String>> pairs, double[] rates) {
        Map<String, Map<String, Double>> g = new HashMap<>();
        for (int i = 0; i < pairs.size(); i++) {
            String a = pairs.get(i).get(0), b = pairs.get(i).get(1);
            g.computeIfAbsent(a, k -> new HashMap<>()).put(b, rates[i]);
            g.computeIfAbsent(b, k -> new HashMap<>()).put(a, 1.0 / rates[i]);
        }
        return g;
    }

    private Map<String, Double> bellman(String start, List<List<String>> pairs, double[] rates) {
        Map<String, Map<String, Double>> g = buildRateGraph(pairs, rates);
        Map<String, Double> dist = new HashMap<>();
        dist.put(start, 1.0);
        for (int it = 0; it < 100; it++) {
            boolean updated = false;
            for (Map.Entry<String, Map<String, Double>> fromKv : g.entrySet()) {
                String from = fromKv.getKey();
                if (!dist.containsKey(from) || dist.get(from) == 0) continue;
                for (Map.Entry<String, Double> toKv : fromKv.getValue().entrySet()) {
                    double nv = dist.get(from) * toKv.getValue();
                    if (!dist.containsKey(toKv.getKey()) || nv > dist.get(toKv.getKey())) {
                        dist.put(toKv.getKey(), nv);
                        updated = true;
                    }
                }
            }
            if (!updated) break;
        }
        return dist;
    }

    public double maxAmount(String initialCurrency, List<List<String>> pairs1, double[] rates1,
                            List<List<String>> pairs2, double[] rates2) {
        Map<String, Double> amt1 = bellman(initialCurrency, pairs1, rates1);
        double ans = 1.0;
        Map<String, Map<String, Double>> g2 = buildRateGraph(pairs2, rates2);
        for (Map.Entry<String, Double> kv : amt1.entrySet()) {
            String c = kv.getKey();
            double a = kv.getValue();
            if (a <= 0) continue;
            Map<String, Double> dist = new HashMap<>();
            dist.put(c, a);
            boolean updated = true;
            for (int it = 0; it < 100 && updated; it++) {
                updated = false;
                for (Map.Entry<String, Map<String, Double>> fromKv : g2.entrySet()) {
                    String from = fromKv.getKey();
                    if (!dist.containsKey(from) || dist.get(from) == 0) continue;
                    for (Map.Entry<String, Double> toKv : fromKv.getValue().entrySet()) {
                        double nv = dist.get(from) * toKv.getValue();
                        if (!dist.containsKey(toKv.getKey()) || nv > dist.get(toKv.getKey())) {
                            dist.put(toKv.getKey(), nv);
                            updated = true;
                        }
                    }
                }
            }
            if (dist.containsKey(initialCurrency) && dist.get(initialCurrency) > ans) {
                ans = dist.get(initialCurrency);
            }
        }
        return ans;
    }
}
