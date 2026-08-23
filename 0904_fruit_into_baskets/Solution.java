// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

import java.util.*;

class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> count = new HashMap<>();
        int left = 0, ans = 0;
        for (int right = 0; right < fruits.length; right++) {
            count.put(fruits[right], count.getOrDefault(fruits[right], 0) + 1);
            while (count.size() > 2) {
                int c = count.get(fruits[left]) - 1;
                if (c == 0) count.remove(fruits[left]);
                else count.put(fruits[left], c);
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
