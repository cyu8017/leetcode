// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumInvitations = function(grid) {
    const boys = grid.length;
    const girls = grid[0].length;
    const matchGirl = new Array(girls).fill(-1);

    const dfs = (boy, seen) => {
        for (let girl = 0; girl < girls; girl++) {
            if (grid[boy][girl] && !seen[girl]) {
                seen[girl] = true;
                if (matchGirl[girl] === -1 || dfs(matchGirl[girl], seen)) {
                    matchGirl[girl] = boy;
                    return true;
                }
            }
        }
        return false;
    };

    let ans = 0;
    for (let boy = 0; boy < boys; boy++) {
        if (dfs(boy, new Array(girls).fill(false))) ans += 1;
    }
    return ans;
};
