// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countDistinctIntegers(int[] nums) {
        int rev(int x) {
            int r = 0;
            while (x > 0) {
                r = r * 10 + x % 10;
                x /= 10;
            }
            return r;
        }
        var seen = new HashSet<Integer>();
        for (int x : nums) {
            seen.add(x);
            seen.add(Rev(x));
        }
        return seen.size();
    }
}
