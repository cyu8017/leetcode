// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

using System.Collections.Generic;

public class Solution {
    public bool CanAliceWin(IList<string> a, IList<string> b) {
        int i = 0, j = 0;
        char last = (char)0;
        bool alice = true;
        while (true) {
            if (alice) {
                while (i < a.Count && a[i][0] <= last) i++;
                if (i == a.Count) return false;
                last = a[i][a[i].Length - 1];
                i++;
            } else {
                while (j < b.Count && b[j][0] <= last) j++;
                if (j == b.Count) return true;
                last = b[j][b[j].Length - 1];
                j++;
            }
            alice = !alice;
        }
    }
}
