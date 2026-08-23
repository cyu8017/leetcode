// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

import java.util.*;

class Solution {
    public List<Long> maximumEvenSplit(long finalSum) {
        if (finalSum % 2 != 0) return new ArrayList<>();
        List<Long> ans = new ArrayList<>();
        for (long x = 2; x <= finalSum; x += 2) {
            ans.add(x);
            finalSum -= x;
        }
        ans.set(ans.size() - 1, ans.get(ans.size() - 1) + finalSum);
        return ans;
    }
}
