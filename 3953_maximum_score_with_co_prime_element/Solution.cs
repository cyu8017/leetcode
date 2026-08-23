// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

using System.Collections.Generic;

public class Solution {
    public int MaxScore(int[] nums, int maxVal) {
        int limit = maxVal;
        int[] frequency = new int[100001];
        foreach (int x in nums) {
            frequency[x]++;
            if (x > limit) limit = x;
        }
        int[] divisible = new int[limit + 1];
        for (int d = 1; d <= limit; d++) {
            for (int multiple = d; multiple <= limit; multiple += d) {
                if (multiple < frequency.Length) divisible[d] += frequency[multiple];
            }
        }
        int BadCount(int x) {
            var primes = new List<int>();
            int y = x;
            for (int p = 2; 1L * p * p <= y; p++) {
                if (y % p == 0) {
                    primes.Add(p);
                    while (y % p == 0) y /= p;
                }
            }
            if (y > 1) primes.Add(y);
            int bad = 0;
            int psz = primes.Count;
            for (int mask = 1; mask < (1 << psz); mask++) {
                int product = 1, bits = 0;
                for (int i = 0; i < psz; i++) {
                    if (((mask >> i) & 1) != 0) {
                        product *= primes[i];
                        bits++;
                    }
                }
                if (bits % 2 == 1) bad += divisible[product];
                else bad -= divisible[product];
            }
            return bad;
        }
        int best = -nums.Length;
        bool[] checkedArr = new bool[limit + 1];
        void Evaluate(int x, bool exists) {
            if (checkedArr[x]) return;
            checkedArr[x] = true;
            int bad = BadCount(x);
            int cost = 0;
            if (exists) {
                if (x > 1) cost = bad - 1;
            } else if (bad > 0) cost = bad;
            else cost = 1;
            if (x - cost > best) best = x - cost;
        }
        for (int x = 1; x <= maxVal; x++) {
            Evaluate(x, x < frequency.Length && frequency[x] > 0);
        }
        foreach (int x in nums) Evaluate(x, true);
        return best;
    }
}
