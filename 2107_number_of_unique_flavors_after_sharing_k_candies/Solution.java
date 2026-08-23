// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

import java.util.*;

class Solution {
    public int shareCandies(int[] candies, int k) {
        int n = candies.length;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int c : candies) freq.merge(c, 1, Integer::sum);
        if (k == 0) return freq.size();
        for (int i = 0; i < k; i++) {
            int c = candies[i];
            if (freq.merge(c, -1, Integer::sum) == 0) freq.remove(c);
        }
        int ans = freq.size();
        for (int i = k; i < n; i++) {
            freq.merge(candies[i - k], 1, Integer::sum);
            int c = candies[i];
            if (freq.merge(c, -1, Integer::sum) == 0) freq.remove(c);
            ans = Math.max(ans, freq.size());
        }
        return ans;
    }
}
