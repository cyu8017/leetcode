// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private static List<Integer> GOOD;
    private static boolean ready = false;

    private static void init() {
        if (ready) return;
        final long LIMIT = 1000000000L;
        Map<Integer, Integer> cnt = new HashMap<>();
        long[] cubes = new long[1001];
        for (int i = 0; i <= 1000; i++) cubes[i] = 1L * i * i * i;
        for (int a = 1; a <= 1000; a++) {
            for (int b = a; b <= 1000; b++) {
                long x = cubes[a] + cubes[b];
                if (x > LIMIT) break;
                int xi = (int) x;
                cnt.put(xi, cnt.getOrDefault(xi, 0) + 1);
            }
        }
        GOOD = new ArrayList<>();
        for (Map.Entry<Integer, Integer> kv : cnt.entrySet()) {
            if (kv.getValue() > 1) GOOD.add(kv.getKey());
        }
        Collections.sort(GOOD);
        ready = true;
    }

    public int[] findGoodIntegers(int n) {
        init();
        int lo = 0, hi = GOOD.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (GOOD.get(mid) <= n) lo = mid + 1;
            else hi = mid;
        }
        int[] ans = new int[lo];
        for (int i = 0; i < lo; i++) ans[i] = GOOD.get(i);
        return ans;
    }
}
