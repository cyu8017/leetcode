// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

class Solution {
    private String toBin(int x) {
        if (x == 0) return "0";
        StringBuilder s = new StringBuilder();
        while (x > 0) {
            s.insert(0, (char) ('0' + (x & 1)));
            x >>= 1;
        }
        return s.toString();
    }

    public int maxGoodNumber(int[] nums) {
        String[] bs = new String[3];
        for (int i = 0; i < 3; i++) bs[i] = toBin(nums[i]);
        int[] idx = {0, 1, 2};
        int[] ans = {0};
        perm(0, idx, bs, ans);
        return ans[0];
    }

    private void perm(int i, int[] idx, String[] bs, int[] ans) {
        if (i == 3) {
            String s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]];
            int v = 0;
            for (char c : s.toCharArray()) v = v * 2 + (c - '0');
            if (v > ans[0]) ans[0] = v;
            return;
        }
        for (int j = i; j < 3; j++) {
            int t = idx[i]; idx[i] = idx[j]; idx[j] = t;
            perm(i + 1, idx, bs, ans);
            t = idx[i]; idx[i] = idx[j]; idx[j] = t;
        }
    }
}
