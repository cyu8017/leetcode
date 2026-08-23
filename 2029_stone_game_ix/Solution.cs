// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

using System;

public class Solution {
    public bool StoneGameIX(int[] stones) {
        int[] cnt = new int[3];
        foreach (int s in stones) cnt[s % 3]++;
        if (cnt[0] % 2 == 0) return cnt[1] > 0 && cnt[2] > 0;
        return Math.Abs(cnt[1] - cnt[2]) > 2;
    }
}
