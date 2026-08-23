// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        int n = nums.length;
        boolean[] mark = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (nums[i] == key) {
                int l = Math.max(0, i - k), r = Math.min(n - 1, i + k);
                for (int j = l; j <= r; j++) mark[j] = true;
            }
        }
        var ans = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) if (mark[i]) ans.add(i);
        return ans;
    }
}
