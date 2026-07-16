// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

public class Solution {
    public int CountArrangement(int n) {
        return Backtrack(1, n, new HashSet<int>());
    }

    private static int Backtrack(int index, int n, HashSet<int> used) {
        if (index == n + 1) {
            return 1;
        }
        int count = 0;
        for (int num = 1; num <= n; num++) {
            if (used.Contains(num)) {
                continue;
            }
            if (index % num == 0 || num % index == 0) {
                used.Add(num);
                count += Backtrack(index + 1, n, used);
                used.Remove(num);
            }
        }
        return count;
    }
}
