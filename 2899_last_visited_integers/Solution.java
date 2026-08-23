// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> lastVisitedIntegers(int[] nums) {
        List<Integer> seen = new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        int k = 0;
        for (int v : nums) {
            if (v != -1) {
                seen.add(v);
                k = 0;
            } else {
                k++;
                if (k > seen.size()) ans.add(-1);
                else ans.add(seen.get(seen.size() - k));
            }
        }
        return ans;
    }
}
