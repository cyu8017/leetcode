// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

using System.Collections.Generic;

public class Solution {
    static List<int> GOOD;
    static bool ready = false;

    static void Init() {
        if (ready) return;
        const long LIMIT = 1000000000L;
        var cnt = new Dictionary<int, int>();
        var cubes = new long[1001];
        for (int i = 0; i <= 1000; i++) cubes[i] = 1L * i * i * i;
        for (int a = 1; a <= 1000; a++) {
            for (int b = a; b <= 1000; b++) {
                long x = cubes[a] + cubes[b];
                if (x > LIMIT) break;
                int xi = (int)x;
                if (!cnt.ContainsKey(xi)) cnt[xi] = 0;
                cnt[xi]++;
            }
        }
        GOOD = new List<int>();
        foreach (var kv in cnt) {
            if (kv.Value > 1) GOOD.Add(kv.Key);
        }
        GOOD.Sort();
        ready = true;
    }

    public int[] FindGoodIntegers(int n) {
        Init();
        int lo = 0, hi = GOOD.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (GOOD[mid] <= n) lo = mid + 1;
            else hi = mid;
        }
        var ans = new int[lo];
        for (int i = 0; i < lo; i++) ans[i] = GOOD[i];
        return ans;
    }
}
