// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

public class Solution {
    public int MaximumInvitations(int[][] grid) {
        int boys = grid.Length, girls = grid[0].Length;
        int[] matchGirl = new int[girls];
        for (int i = 0; i < girls; i++) matchGirl[i] = -1;

        bool Dfs(int boy, bool[] seen) {
            for (int girl = 0; girl < girls; girl++) {
                if (grid[boy][girl] == 1 && !seen[girl]) {
                    seen[girl] = true;
                    if (matchGirl[girl] == -1 || Dfs(matchGirl[girl], seen)) {
                        matchGirl[girl] = boy;
                        return true;
                    }
                }
            }
            return false;
        }

        int ans = 0;
        for (int boy = 0; boy < boys; boy++) {
            if (Dfs(boy, new bool[girls])) ans++;
        }
        return ans;
    }
}
