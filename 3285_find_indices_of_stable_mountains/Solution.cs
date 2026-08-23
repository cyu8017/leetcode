// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

using System.Collections.Generic;

public class Solution {
    public IList<int> StableMountains(int[] height, int threshold) {
        var ans = new List<int>();
        for (int i = 1; i < height.Length; i++) {
            if (height[i - 1] > threshold) ans.Add(i);
        }
        return ans;
    }
}
