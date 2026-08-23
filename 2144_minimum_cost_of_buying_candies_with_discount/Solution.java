// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

import java.util.Arrays;

class Solution {
    public int minimumCost(int[] cost) {
        Integer[] arr = Arrays.stream(cost).boxed().toArray(Integer[]::new);
        Arrays.sort(arr, (a, b) -> Integer.compare(b, a));
        int ans = 0;
        for (int i = 0; i < arr.length; i++)
            if (i % 3 != 2) ans += arr[i];
        return ans;
    }
}
