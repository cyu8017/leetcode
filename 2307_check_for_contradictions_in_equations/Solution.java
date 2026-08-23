// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private Map<String, String> parent;
    private Map<String, Double> weight;

    public boolean checkContradictions(List<List<String>> equations, double[] values) {
        parent = new HashMap<>();
        weight = new HashMap<>();
        for (int i = 0; i < equations.size(); ++i) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            String ra = find(a), rb = find(b);
            if (ra.equals(rb)) {
                if (Math.abs(weight.get(a) / weight.get(b) - values[i]) > 1e-5) return true;
            } else {
                parent.put(ra, rb);
                weight.put(ra, values[i] * weight.get(b) / weight.get(a));
            }
        }
        return false;
    }

    private String find(String x) {
        if (!parent.containsKey(x)) {
            parent.put(x, x);
            weight.put(x, 1.0);
            return x;
        }
        if (!parent.get(x).equals(x)) {
            String p = find(parent.get(x));
            weight.put(x, weight.get(x) * weight.get(parent.get(x)));
            parent.put(x, p);
        }
        return parent.get(x);
    }
}
