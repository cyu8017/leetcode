// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool PrimeSubOperation(int[] nums) {
        int maxV = nums.Max();
        bool[] isP = new bool[maxV + 1];
        for (int i = 0; i <= maxV; i++) isP[i] = true;
        if (maxV >= 0) isP[0] = false;
        if (maxV >= 1) isP[1] = false;
        for (int i = 2; i * i <= maxV; ++i) {
            if (isP[i]) {
                for (int j = i * i; j <= maxV; j += i) isP[j] = false;
            }
        }
        var primes = new List<int>();
        for (int i = 2; i <= maxV; ++i) if (isP[i]) primes.Add(i);
        int prev = 0;
        foreach (int x in nums) {
            if (x <= prev) return false;
            int best = x;
            foreach (int p in primes) {
                if (p >= x) break;
                if (x - p > prev) best = x - p;
            }
            prev = best;
        }
        return true;
    }
}
