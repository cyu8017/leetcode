// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private int makePal(int x) {
        char[] ch = Integer.toString(x).toCharArray();
        for (int i = 0, j = ch.length - 1; i < j; i++, j--) ch[j] = ch[i];
        return Integer.parseInt(new String(ch));
    }

    private long cost(int[] nums, int p) {
        long c = 0;
        for (int v : nums) c += Math.abs((long) v - p);
        return c;
    }

    public long minimumCost(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int median = nums[n / 2];
        List<Integer> candidates = new ArrayList<>();
        candidates.add(makePal(median));
        String s = Integer.toString(median);
        int half = Integer.parseInt(s.substring(0, (s.length() + 1) / 2));
        for (int d = -2; d <= 2; d++) {
            int h = half + d;
            if (h <= 0) continue;
            String hs = Integer.toString(h);
            String pal;
            if (s.length() % 2 == 0) {
                char[] rb = hs.toCharArray();
                for (int i = 0, j = rb.length - 1; i < j; i++, j--) {
                    char tmp = rb[i]; rb[i] = rb[j]; rb[j] = tmp;
                }
                pal = hs + new String(rb);
            } else {
                String prefix = hs.substring(0, hs.length() - 1);
                char[] rb = prefix.toCharArray();
                for (int i = 0, j = rb.length - 1; i < j; i++, j--) {
                    char tmp = rb[i]; rb[i] = rb[j]; rb[j] = tmp;
                }
                pal = hs + new String(rb);
            }
            try {
                candidates.add(Integer.parseInt(pal));
            } catch (NumberFormatException ignored) {}
        }
        for (int v : new int[]{1, 9, 11, 99, 101}) candidates.add(v);
        long ans = Long.MAX_VALUE / 4;
        for (int p : candidates) {
            if (p <= 0) continue;
            ans = Math.min(ans, cost(nums, p));
        }
        return ans;
    }
}
