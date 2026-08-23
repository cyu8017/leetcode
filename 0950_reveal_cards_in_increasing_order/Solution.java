// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

import java.util.*;

class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        int n = deck.length;
        Deque<Integer> idx = new ArrayDeque<>();
        for (int i = 0; i < n; i++) idx.addLast(i);
        int[] ans = new int[n];
        for (int card : deck) {
            ans[idx.removeFirst()] = card;
            if (!idx.isEmpty()) idx.addLast(idx.removeFirst());
        }
        return ans;
    }
}
