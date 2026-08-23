// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

using System;

public class Solution {
    struct Enemy { public int dmg, hits; public Enemy(int dmg, int hits) { this.dmg = dmg; this.hits = hits; } }

    public long MinDamage(int power, int[] damage, int[] health) {
        int n = damage.Length;
        var arr = new Enemy[n];
        int totalDmg = 0;
        for (int i = 0; i < n; i++) {
            int hits = (health[i] + power - 1) / power;
            arr[i] = new Enemy(damage[i], hits);
            totalDmg += damage[i];
        }
        Array.Sort(arr, (a, b) => ((long)a.hits * b.dmg).CompareTo((long)b.hits * a.dmg));
        long ans = 0, cur = totalDmg;
        foreach (var e in arr) {
            ans += cur * e.hits;
            cur -= e.dmg;
        }
        return ans;
    }
}
