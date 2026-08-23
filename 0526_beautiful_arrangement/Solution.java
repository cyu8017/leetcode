// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countArrangement(int n) {
        return backtrack(1, n, new HashSet<>());
    }

    private int backtrack(int index, int n, Set<Integer> used) {
        if (index == n + 1) {
            return 1;
        }
        int count = 0;
        for (int num = 1; num <= n; num++) {
            if (used.contains(num)) {
                continue;
            }
            if (index % num == 0 || num % index == 0) {
                used.add(num);
                count += backtrack(index + 1, n, used);
                used.remove(num);
            }
        }
        return count;
    }
}
