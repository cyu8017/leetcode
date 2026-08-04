// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

import java.util.*;

class Solution {
    public int countElements(int[] arr) {
        Set<Integer> values = new HashSet<>();
        for (int value : arr) values.add(value);
        int ans = 0;
        for (int value : arr) if (values.contains(value + 1)) ans++;
        return ans;
    }
}
