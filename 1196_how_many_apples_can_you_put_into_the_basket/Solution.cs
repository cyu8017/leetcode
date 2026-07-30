// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

using System;
using System.Linq;

public class Solution {
    public int MaxNumberOfApples(int[] weight) {
        Array.Sort(weight);
        int total = 0;
        for (int i = 0; i < weight.Length; i++) {
            total += weight[i];
            if (total > 5000) return i;
        }
        return weight.Length;
    }
}
