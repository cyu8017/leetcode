// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean splitArray(int[] nums) {
        int n = nums.length;
        if (n < 7) {
            return false;
        }

        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        for (int j = 3; j < n - 3; j++) {
            Set<Integer> seen = new HashSet<>();
            for (int i = 1; i < j - 1; i++) {
                int first = prefix[i] - prefix[0];
                int second = prefix[j] - prefix[i + 1];
                if (first == second) {
                    seen.add(first);
                }
            }

            for (int k = j + 2; k < n - 1; k++) {
                int third = prefix[k] - prefix[j + 1];
                int fourth = prefix[n] - prefix[k + 1];
                if (third == fourth && seen.contains(third)) {
                    return true;
                }
            }
        }

        return false;
    }
}
