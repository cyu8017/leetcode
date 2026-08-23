// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum_sum_of_three_numbers_divisible_by_three/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int maximumSum(int[] nums) {
        Arrays.sort(nums);
        List<Integer>[] g = newList(3);
        for (int x : nums) g[x % 3].add(x);
        int ans = 0;
        for (int a = 0; a < 3; a++) {
            if (!g[a].isEmpty()) {
                int x = g[a].remove(g[a].size() - 1);
                for (int b = 0; b < 3; b++) {
                    if (!g[b].isEmpty()) {
                        int y = g[b].remove(g[b].size() - 1);
                        int c = (3 - (a + b) % 3) % 3;
                        if (!g[c].isEmpty()) {
                            int z = g[c].get(g[c].size() - 1);
                            ans = Math.max(ans, x + y + z);
                        }
                        g[b].add(y);
                    }
                }
                g[a].add(x);
            }
        }
        return ans;
    }

    @SuppressWarnings("unchecked")
    private List<Integer>[] newList(int n) {
        List<Integer>[] g = (List<Integer>[]) new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        return g;
    }
}
