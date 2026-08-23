// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

using System.Collections.Generic;

public class Solution {
    bool IsPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++)
            if (x % i == 0) return false;
        return true;
    }
    public bool CheckPrimeFrequency(int[] nums) {
        var cnt = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
        }
        foreach (var kv in cnt)
            if (IsPrime(kv.Value)) return true;
        return false;
    }
}
