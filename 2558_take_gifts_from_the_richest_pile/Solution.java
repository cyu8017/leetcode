// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

import java.util.PriorityQueue;

class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> h = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        for (int g : gifts) h.offer(g);
        for (int i = 0; i < k; ++i) {
            int x = h.poll();
            h.offer((int) Math.sqrt(x));
        }
        long ans = 0;
        while (!h.isEmpty()) ans += h.poll();
        return ans;
    }
}
