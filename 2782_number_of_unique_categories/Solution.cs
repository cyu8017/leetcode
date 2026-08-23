// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

using System.Collections.Generic;

public class Solution {
    public int NumberOfCategories(int n, int[] categoryHandler) {
        return new HashSet<int>(categoryHandler).Count;
    }
}
