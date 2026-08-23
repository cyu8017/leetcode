// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

using System.Collections.Generic;

public class Solution {
    public bool IsNStraightHand(int[] hand, int groupSize) {
        if (hand.Length % groupSize != 0) return false;
        var count = new SortedDictionary<int, int>();
        foreach (int x in hand) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }
        var keys = new List<int>(count.Keys);
        foreach (int start in keys) {
            while (count.ContainsKey(start) && count[start] > 0) {
                for (int x = start; x < start + groupSize; x++) {
                    if (!count.ContainsKey(x) || count[x] == 0) return false;
                    if (--count[x] == 0) count.Remove(x);
                }
            }
        }
        return true;
    }
}
