// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution {
    public int maximumRemovals(String s, String p, int[] removable) {
        int lo = 0;
        int hi = removable.length;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (stillSubsequence(s, p, removable, mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }

    private boolean stillSubsequence(String s, String p, int[] removable, int k) {
        boolean[] removed = new boolean[s.length()];
        for (int i = 0; i < k; i++) {
            removed[removable[i]] = true;
        }
        int index = 0;
        for (int position = 0; position < s.length(); position++) {
            if (removed[position]) {
                continue;
            }
            if (index < p.length() && s.charAt(position) == p.charAt(index)) {
                index++;
            }
        }
        return index == p.length();
    }
}
