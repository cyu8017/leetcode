// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> findPrimePairs(int n) {
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) isPrime[i] = true;
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) isPrime[j] = false;
            }
        }
        var ans = new ArrayList<List<Integer>>();
        for (int x = 2; x <= n / 2; x++) {
            int y = n - x;
            if (isPrime[x] && isPrime[y]) ans.add(new ArrayList<>(Arrays.asList(x, y)));
        }
        return ans;
    }
}
