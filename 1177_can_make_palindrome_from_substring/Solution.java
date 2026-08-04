// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

import java.util.*;

class Solution {
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        int[] prefix = new int[s.length() + 1];
        int mask = 0;
        for (int i = 0; i < s.length(); i++) {
            mask ^= 1 << (s.charAt(i) - 'a');
            prefix[i + 1] = mask;
        }
        List<Boolean> ans = new ArrayList<>();
        for (int[] q : queries) {
            int bits = Integer.bitCount(prefix[q[1] + 1] ^ prefix[q[0]]);
            ans.add(bits / 2 <= q[2]);
        }
        return ans;
    }
}
