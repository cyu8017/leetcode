// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

import java.util.HashMap;
import java.util.Map;

class Solution {
    boolean isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++)
            if (x % i == 0) return false;
        return true;
    }
    public boolean checkPrimeFrequency(int[] nums) {
        var cnt = new HashMap<Integer, Integer>();
        for (int x : nums) {
            if (!cnt.containsKey(x)) cnt.put(x, 0);
            cnt.put(x, cnt.get(x) + 1);
        }
        for (var kv : cnt.entrySet())
            if (isPrime(kv.getValue())) return true;
        return false;
    }
}
