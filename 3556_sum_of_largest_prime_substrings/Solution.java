// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    boolean isPrime(long x) {
        if (x < 2) return false;
        long sqrtX = (long)Math.sqrt(x);
        for (long i = 2; i <= sqrtX; i++) if (x % i == 0) return false;
        return true;
    }
    public long sumOfLargestPrimes(String s) {
        var st = new HashSet<Long>();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            long x = 0;
            for (int j = i; j < n; j++) {
                x = x * 10 + (s.charAt(j) - '0');
                if (isPrime(x)) st.add(x);
            }
        }
        var nums = new ArrayList<Long>(st);
        nums.sort(null);
        long ans = 0;
        for (int i = nums.size() - 1; i >= 0 && nums.size() - i <= 3; i--)
            ans += nums.get(i);
        return ans;
    }
}
