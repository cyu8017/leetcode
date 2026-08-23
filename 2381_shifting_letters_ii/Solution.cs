// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

public class Solution {
    public string ShiftingLetters(string s, int[][] shifts) {
        int n = s.Length;
        int[] diff = new int[n + 1];
        foreach (var sh in shifts) {
            int d = sh[2] == 0 ? -1 : 1;
            diff[sh[0]] += d;
            diff[sh[1] + 1] -= d;
        }
        char[] arr = s.ToCharArray();
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur = (cur + diff[i]) % 26;
            if (cur < 0) cur += 26;
            arr[i] = (char)('a' + (arr[i] - 'a' + cur) % 26);
        }
        return new string(arr);
    }
}
