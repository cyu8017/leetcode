// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

using System.Collections.Generic;

public class Solution {
    public int TupleSameProduct(int[] nums) {
        var counts = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            for (int j = i + 1; j < nums.Length; j++) {
                int product = nums[i] * nums[j];
                counts.TryGetValue(product, out int current);
                counts[product] = current + 1;
            }
        }
        long result = 0;
        foreach (int count in counts.Values) {
            result += (long)count * (count - 1) * 4;
        }
        return (int)result;
    }
}
