// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

public class Solution {
    public int[] Decode(int[] encoded) {
        int n = encoded.Length + 1;
        int total = 0;
        for (int value = 1; value <= n; value++) {
            total ^= value;
        }
        int odd = 0;
        for (int i = 1; i < encoded.Length; i += 2) {
            odd ^= encoded[i];
        }
        int[] ans = new int[n];
        ans[0] = total ^ odd;
        for (int i = 0; i < encoded.Length; i++) {
            ans[i + 1] = ans[i] ^ encoded[i];
        }
        return ans;
    }
}
