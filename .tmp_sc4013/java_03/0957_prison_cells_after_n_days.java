// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

import java.util.*;

class Solution {
    public int[] prisonAfterNDays(int[] cells, int n) {
        Map<String, Integer> seen = new HashMap<>();
        int[] state = cells.clone();
        while (n > 0) {
            String key = Arrays.toString(state);
            if (seen.containsKey(key)) {
                int cycle = seen.get(key) - n;
                n %= cycle;
                if (n == 0) break;
            }
            seen.put(key, n);
            int[] nxt = new int[8];
            for (int i = 1; i <= 6; i++) nxt[i] = state[i - 1] == state[i + 1] ? 1 : 0;
            state = nxt;
            n--;
        }
        return state;
    }
}
