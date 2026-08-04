// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

import java.util.*;

class Solution {
    public int maxNumberOfApples(int[] weight) {
        Arrays.sort(weight);
        int total = 0;
        for (int i = 0; i < weight.length; i++) {
            total += weight[i];
            if (total > 5000) return i;
        }
        return weight.length;
    }
}
