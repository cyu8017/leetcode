// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

class Solution {
    fun maximumInvitations(grid: Array<IntArray>): Int {
        val boys = grid.size
        val girls = grid[0].size
        val matchGirl = IntArray(girls) { -1 }

        fun dfs(boy: Int, seen: BooleanArray): Boolean {
            for (girl in 0 until girls) {
                if (grid[boy][girl] == 1 && !seen[girl]) {
                    seen[girl] = true
                    if (matchGirl[girl] == -1 || dfs(matchGirl[girl], seen)) {
                        matchGirl[girl] = boy
                        return true
                    }
                }
            }
            return false
        }

        var ans = 0
        for (boy in 0 until boys) {
            if (dfs(boy, BooleanArray(girls))) ans++
        }
        return ans
    }
}
