// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

import java.util.Arrays;

class Solution {
    public int maximumInvitations(int[][] grid) {
        int boys = grid.length;
        int girls = grid[0].length;
        int[] matchGirl = new int[girls];
        Arrays.fill(matchGirl, -1);

        int ans = 0;
        for (int boy = 0; boy < boys; boy++) {
            if (dfs(grid, boy, new boolean[girls], matchGirl)) {
                ans++;
            }
        }
        return ans;
    }

    private boolean dfs(int[][] grid, int boy, boolean[] seen, int[] matchGirl) {
        for (int girl = 0; girl < grid[0].length; girl++) {
            if (grid[boy][girl] == 1 && !seen[girl]) {
                seen[girl] = true;
                if (matchGirl[girl] == -1 || dfs(grid, matchGirl[girl], seen, matchGirl)) {
                    matchGirl[girl] = boy;
                    return true;
                }
            }
        }
        return false;
    }
}
