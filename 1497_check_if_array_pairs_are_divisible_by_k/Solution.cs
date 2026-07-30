// LeetCode 1497 - Check If Array Pairs Are Divisible By K
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

public class Solution {
    public bool CanArrange(int[] arr, int k) {
        var count = new int[k];
        foreach (int x in arr) count[((x % k) + k) % k]++;
        if (count[0] % 2 != 0) return false;
        for (int r = 1; r < k; r++) if (count[r] != count[k - r]) return false;
        return true;
    }
}
