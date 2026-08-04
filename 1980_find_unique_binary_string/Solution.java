// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

import java.util.*;

class Solution {
    public String findDifferentBinaryString(String[] nums) {
        Set<String> set = new HashSet<>(Arrays.asList(nums));
        int n = nums.length;
        for (int i = 0; i < (1 << n); i++) {
            StringBuilder sb = new StringBuilder();
            for (int b = n - 1; b >= 0; b--) sb.append((i >> b) & 1);
            String cand = sb.toString();
            if (!set.contains(cand)) return cand;
        }
        return "0".repeat(n);
    }
}
