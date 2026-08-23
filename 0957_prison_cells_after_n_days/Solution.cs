// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

using System.Collections.Generic;

public class Solution {
    public int[] PrisonAfterNDays(int[] cells, int n) {
        var seen = new Dictionary<string, int>();
        int[] state = (int[])cells.Clone();
        while (n > 0) {
            string key = string.Join(",", state);
            if (seen.ContainsKey(key)) {
                int cycle = seen[key] - n;
                n %= cycle;
                if (n == 0) break;
            }
            seen[key] = n;
            int[] nxt = new int[8];
            for (int i = 1; i <= 6; i++) nxt[i] = state[i - 1] == state[i + 1] ? 1 : 0;
            state = nxt;
            n--;
        }
        return state;
    }
}
