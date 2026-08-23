// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] maxHammingDistances(int[] nums, int m) {
        int[] dist = new int[1 << m];
        Arrays.fill(dist, -1);
        List<Integer> q = new ArrayList<>();
        for (int x : nums) {
            dist[x] = 0;
            q.add(x);
        }
        for (int k = 1; !q.isEmpty(); k++) {
            List<Integer> t = new ArrayList<>();
            for (int x : q) {
                for (int i = 0; i < m; i++) {
                    int y = x ^ (1 << i);
                    if (dist[y] == -1) {
                        dist[y] = k;
                        t.add(y);
                    }
                }
            }
            q = t;
        }
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            nums[i] = m - dist[x ^ ((1 << m) - 1)];
        }
        return nums;
    }
}
