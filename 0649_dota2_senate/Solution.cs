// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

using System.Collections.Generic;

public class Solution {
    public string PredictPartyVictory(string senate) {
        var radiant = new Queue<int>();
        var dire = new Queue<int>();
        int n = senate.Length;
        for (int i = 0; i < n; ++i) {
            if (senate[i] == 'R') radiant.Enqueue(i);
            else dire.Enqueue(i);
        }
        while (radiant.Count > 0 && dire.Count > 0) {
            int r = radiant.Dequeue();
            int d = dire.Dequeue();
            if (r < d) radiant.Enqueue(r + n);
            else dire.Enqueue(d + n);
        }
        return radiant.Count == 0 ? "Dire" : "Radiant";
    }
}
