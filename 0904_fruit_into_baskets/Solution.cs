// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

using System;
using System.Collections.Generic;

public class Solution {
    public int TotalFruit(int[] fruits) {
        var count = new Dictionary<int, int>();
        int left = 0, ans = 0;
        for (int right = 0; right < fruits.Length; right++) {
            if (!count.ContainsKey(fruits[right])) count[fruits[right]] = 0;
            count[fruits[right]]++;
            while (count.Count > 2) {
                if (--count[fruits[left]] == 0) count.Remove(fruits[left]);
                left++;
            }
            ans = Math.Max(ans, right - left + 1);
        }
        return ans;
    }
}
