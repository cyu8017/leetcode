// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] DeckRevealedIncreasing(int[] deck) {
        Array.Sort(deck);
        int n = deck.Length;
        var idx = new LinkedList<int>();
        for (int i = 0; i < n; i++) idx.AddLast(i);
        int[] ans = new int[n];
        foreach (int card in deck) {
            ans[idx.First.Value] = card;
            idx.RemoveFirst();
            if (idx.Count > 0) {
                idx.AddLast(idx.First.Value);
                idx.RemoveFirst();
            }
        }
        return ans;
    }
}
