// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

import java.util.*;

class Solution {
    public int countTriplets(int[] nums) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int a : nums)
            for (int b : nums)
                cnt.merge(a & b, 1, Integer::sum);
        int ans = 0;
        for (int c : nums)
            for (Map.Entry<Integer, Integer> kv : cnt.entrySet())
                if ((kv.getKey() & c) == 0) ans += kv.getValue();
        return ans;
    }
}
