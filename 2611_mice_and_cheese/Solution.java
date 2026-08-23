// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

import java.util.Arrays;

class Solution {
    public int miceAndCheese(int[] reward1, int[] reward2, int k) {
        int n = reward1.length;
        Integer[] diff = new Integer[n];
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += reward2[i];
            diff[i] = reward1[i] - reward2[i];
        }
        Arrays.sort(diff, (a, b) -> Integer.compare(b, a));
        for (int i = 0; i < k; ++i) ans += diff[i];
        return ans;
    }
}
