// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

public class Solution {
    public long MaxProduct(int[] nums) {
        int maxV = 0;
        foreach (int v in nums) if (v > maxV) maxV = v;
        int bitsN = 0;
        for (int x = maxV; x > 0; x >>= 1) bitsN++;
        if (bitsN == 0) bitsN = 1;
        int size = 1 << bitsN;
        int[] best = new int[size];
        foreach (int v in nums) if (v > best[v]) best[v] = v;
        for (int mask = 0; mask < size; mask++) {
            for (int b = 0; b < bitsN; b++) {
                if ((mask & (1 << b)) != 0) {
                    int sub = mask ^ (1 << b);
                    if (best[sub] > best[mask]) best[mask] = best[sub];
                }
            }
        }
        long ans = 0;
        foreach (int v in nums) {
            int comp = (size - 1) ^ v;
            if (best[comp] > 0) {
                long p = (long)v * best[comp];
                if (p > ans) ans = p;
            }
        }
        return ans;
    }
}
