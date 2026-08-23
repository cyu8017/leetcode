// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

import java.util.*;

class Solution {
    public int findFinalValue(int[] nums, int original) {
        Set<Integer> have = new HashSet<>();
        for (int x : nums) have.add(x);
        while (have.contains(original)) original *= 2;
        return original;
    }
}
