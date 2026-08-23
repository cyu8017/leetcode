// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<Integer, Integer> first = new HashMap<>();
    private Map<Integer, Integer> last = new HashMap<>();

    public int findValidSplit(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; ++i) factorize(nums[i], i);
        int far = 0;
        for (int i = 0; i < n - 1; ++i) {
            int x = nums[i];
            for (int p = 2; p * p <= x; ++p) {
                if (x % p == 0) {
                    if (last.get(p) > far) far = last.get(p);
                    while (x % p == 0) x /= p;
                }
            }
            if (x > 1 && last.get(x) > far) far = last.get(x);
            if (far == i) return i;
        }
        return -1;
    }

    private void factorize(int x, int idx) {
        for (int p = 2; p * p <= x; ++p) {
            if (x % p == 0) {
                first.putIfAbsent(p, idx);
                last.put(p, idx);
                while (x % p == 0) x /= p;
            }
        }
        if (x > 1) {
            first.putIfAbsent(x, idx);
            last.put(x, idx);
        }
    }
}
