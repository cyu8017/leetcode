// LeetCode 2337 - Move Pieces to Obtain a String
// https://leetcode.com/problems/move-pieces-to-obtain-a-string/

public class Solution {
    public bool CanChange(string start, string target) {
        int n = start.Length;
        int i = 0, j = 0;
        while (i < n || j < n) {
            while (i < n && start[i] == '_') i++;
            while (j < n && target[j] == '_') j++;
            if (i == n || j == n) return i == n && j == n;
            if (start[i] != target[j]) return false;
            if (start[i] == 'L' && i < j) return false;
            if (start[i] == 'R' && i > j) return false;
            i++;
            j++;
        }
        return true;
    }
}
