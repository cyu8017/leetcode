// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int maxFixedPoints(int[] nums) {
        List<Integer> tails = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i < nums[i]) continue;
            int d = i - nums[i];
            int idx = Collections.binarySearch(tails, d);
            if (idx < 0) idx = ~idx;
            if (idx == tails.size()) tails.add(d);
            else tails.set(idx, d);
        }
        return tails.size();
    }
}
