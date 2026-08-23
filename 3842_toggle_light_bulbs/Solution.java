// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] toggleLightBulbs(int[] bulbs) {
        int[] st = new int[101];
        for (int x : bulbs) st[x] ^= 1;
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < 101; i++) if (st[i] == 1) ans.add(i);
        int[] out = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) out[i] = ans.get(i);
        return out;
    }
}
