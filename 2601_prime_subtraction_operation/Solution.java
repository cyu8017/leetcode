// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public boolean primeSubOperation(int[] nums) {
        int maxV = 0;
        for (int x : nums) if (x > maxV) maxV = x;
        boolean[] isP = new boolean[maxV + 1];
        Arrays.fill(isP, true);
        if (maxV >= 0) isP[0] = false;
        if (maxV >= 1) isP[1] = false;
        for (int i = 2; i * i <= maxV; ++i) {
            if (!isP[i]) continue;
            for (int j = i * i; j <= maxV; j += i) isP[j] = false;
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= maxV; ++i) if (isP[i]) primes.add(i);
        int prev = 0;
        for (int x : nums) {
            int need = x - prev;
            int best = -1;
            for (int p : primes) {
                if (p >= need) break;
                best = p;
            }
            int cur = best < 0 ? x : x - best;
            if (cur <= prev) return false;
            prev = cur;
        }
        return true;
    }
}
