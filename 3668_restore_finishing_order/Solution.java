// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

import java.util.Arrays;

class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {
        int n = order.length;
        int[] d = new int[n + 1];
        for (int i = 0; i < n; i++) d[order[i]] = i;
        Integer[] boxed = new Integer[friends.length];
        for (int i = 0; i < friends.length; i++) boxed[i] = friends[i];
        Arrays.sort(boxed, (a, b) -> Integer.compare(d[a], d[b]));
        for (int i = 0; i < friends.length; i++) friends[i] = boxed[i];
        return friends;
    }
}
