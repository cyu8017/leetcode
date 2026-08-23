// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int numberOfCategories(int n, int[] categoryHandler) {
        return new HashSet<Integer>(categoryHandler).size();
    }
}
