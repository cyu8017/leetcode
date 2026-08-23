// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public long countGoodIntegers(int n, int k) {
        int half = (n + 1) / 2;
        int start = 1;
        for (int i = 1; i < half; i++) start *= 10;
        int end = start * 10;
        Set<String> seen = new HashSet<>();
        long ans = 0;
        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;
        for (int h = start; h < end; h++) {
            String s = Integer.toString(h);
            StringBuilder pal = new StringBuilder(s);
            int revStart = s.length() - 1;
            if (n % 2 == 1) revStart--;
            for (int i = revStart; i >= 0; i--) pal.append(s.charAt(i));
            if (Long.parseLong(pal.toString()) % k != 0) continue;
            char[] chars = pal.toString().toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            if (!seen.add(key)) continue;
            int[] cnt = new int[10];
            for (char c : chars) cnt[c - '0']++;
            long total = fact[n];
            for (int c : cnt) total /= fact[c];
            if (cnt[0] > 0) {
                long bad = fact[n - 1];
                cnt[0]--;
                for (int c : cnt) bad /= fact[c];
                cnt[0]++;
                total -= bad;
            }
            ans += total;
        }
        return ans;
    }
}
