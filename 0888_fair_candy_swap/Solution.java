// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

import java.util.*;

class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        int sumA = 0, sumB = 0;
        for (int a : aliceSizes) sumA += a;
        for (int b : bobSizes) sumB += b;
        int diff = (sumA - sumB) / 2;
        Set<Integer> bob = new HashSet<>();
        for (int b : bobSizes) bob.add(b);
        for (int a : aliceSizes) {
            if (bob.contains(a - diff)) return new int[] {a, a - diff};
        }
        return new int[0];
    }
}
