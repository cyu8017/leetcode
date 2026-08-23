// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int maxScore(int[] nums, int maxVal) {
        int limit = maxVal;
        int[] frequency = new int[100001];
        for (int x : nums) {
            frequency[x]++;
            if (x > limit) limit = x;
        }
        int[] divisible = new int[limit + 1];
        for (int d = 1; d <= limit; d++) {
            for (int multiple = d; multiple <= limit; multiple += d) {
                if (multiple < frequency.length) divisible[d] += frequency[multiple];
            }
        }
        int best = -nums.length;
        boolean[] checked = new boolean[limit + 1];
        for (int x = 1; x <= maxVal; x++) {
            best = Math.max(best, evaluate(x, x < frequency.length && frequency[x] > 0, checked, divisible));
        }
        for (int x : nums) {
            best = Math.max(best, evaluate(x, true, checked, divisible));
        }
        return best;
    }

    private int evaluate(int x, boolean exists, boolean[] checked, int[] divisible) {
        if (checked[x]) return Integer.MIN_VALUE / 4;
        checked[x] = true;
        int bad = badCount(x, divisible);
        int cost;
        if (exists) cost = x > 1 ? bad - 1 : 0;
        else cost = bad > 0 ? bad : 1;
        return x - cost;
    }

    private int badCount(int x, int[] divisible) {
        List<Integer> primes = new ArrayList<>();
        int y = x;
        for (int p = 2; 1L * p * p <= y; p++) {
            if (y % p == 0) {
                primes.add(p);
                while (y % p == 0) y /= p;
            }
        }
        if (y > 1) primes.add(y);
        int bad = 0;
        int psz = primes.size();
        for (int mask = 1; mask < (1 << psz); mask++) {
            int product = 1, bits = 0;
            for (int i = 0; i < psz; i++) {
                if (((mask >> i) & 1) != 0) {
                    product *= primes.get(i);
                    bits++;
                }
            }
            if (bits % 2 == 1) bad += divisible[product];
            else bad -= divisible[product];
        }
        return bad;
    }
}
