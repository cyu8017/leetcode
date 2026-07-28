// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] rearrangeBarcodes(int[] barcodes) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int v : barcodes) {
            count.merge(v, 1, Integer::sum);
        }
        List<int[]> pairs = new ArrayList<>();
        for (Map.Entry<Integer, Integer> e : count.entrySet()) {
            pairs.add(new int[] { e.getKey(), e.getValue() });
        }
        pairs.sort((a, b) -> {
            if (a[1] != b[1]) {
                return Integer.compare(b[1], a[1]);
            }
            return Integer.compare(b[0], a[0]);
        });
        int n = barcodes.length;
        int[] ans = new int[n];
        int idx = 0;
        for (int[] p : pairs) {
            for (int k = 0; k < p[1]; k++) {
                ans[idx] = p[0];
                idx += 2;
                if (idx >= n) {
                    idx = 1;
                }
            }
        }
        return ans;
    }
}
