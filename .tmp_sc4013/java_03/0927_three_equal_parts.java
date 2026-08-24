// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

import java.util.*;

class Solution {
    public int[] threeEqualParts(int[] arr) {
        List<Integer> ones = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) if (arr[i] != 0) ones.add(i);
        int n = ones.size();
        if (n % 3 != 0) return new int[] {-1, -1};
        if (n == 0) return new int[] {0, arr.length - 1};
        int third = n / 3;
        int length = ones.get(ones.size() - 1) - ones.get(2 * third) + 1;
        int a = ones.get(0), b = ones.get(third), c = ones.get(2 * third);
        if (a + length > arr.length || b + length > arr.length || c + length > arr.length)
            return new int[] {-1, -1};
        for (int i = 0; i < length; i++) {
            if (arr[a + i] != arr[b + i] || arr[a + i] != arr[c + i]) return new int[] {-1, -1};
        }
        return new int[] {a + length - 1, b + length};
    }
}
