// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

import java.util.*;

class Solution {
    public int binarySearchableNumbers(int[] nums) {
        int n = nums.length;
        boolean[] ok = new boolean[n];
        Arrays.fill(ok, true);
        int mx = Integer.MIN_VALUE, mi = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (nums[i] < mx) ok[i] = false;
            else mx = nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] > mi) ok[i] = false;
            else mi = nums[i];
        }
        int ans = 0;
        for (boolean b : ok) if (b) ans++;
        return ans;
    }
}
