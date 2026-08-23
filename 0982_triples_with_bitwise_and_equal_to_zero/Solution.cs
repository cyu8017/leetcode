// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

using System.Collections.Generic;

public class Solution {
    public int CountTriplets(int[] nums) {
        var cnt = new Dictionary<int, int>();
        foreach (int a in nums)
            foreach (int b in nums) {
                int ab = a & b;
                if (!cnt.ContainsKey(ab)) cnt[ab] = 0;
                cnt[ab]++;
            }
        int ans = 0;
        foreach (int c in nums)
            foreach (var kv in cnt)
                if ((kv.Key & c) == 0) ans += kv.Value;
        return ans;
    }
}
