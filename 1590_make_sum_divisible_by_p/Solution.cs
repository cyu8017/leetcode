// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinSubarray(int[] nums, int p) {
        long total = nums.Sum(x => (long)x);
        int target = (int)(total % p);
        if (target == 0) return 0;
        var seen = new Dictionary<int, int> { [0] = -1 };
        int prefix = 0, answer = nums.Length;
        for (int i = 0; i < nums.Length; i++) {
            prefix = (prefix + nums[i]) % p;
            int need = (prefix - target + p) % p;
            if (seen.ContainsKey(need)) answer = Math.Min(answer, i - seen[need]);
            seen[prefix] = i;
        }
        return answer < nums.Length ? answer : -1;
    }
}
