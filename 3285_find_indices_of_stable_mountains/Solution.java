// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> stableMountains(int[] height, int threshold) {
        var ans = new ArrayList<Integer>();
        for (int i = 1; i < height.length; i++) {
            if (height[i - 1] > threshold) ans.add(i);
        }
        return ans;
    }
}
