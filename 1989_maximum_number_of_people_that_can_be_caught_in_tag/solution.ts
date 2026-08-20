// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

function catchMaximumAmountofPeople(team: number[], dist: number): number {
    let ans = 0, j = 0;
    const n = team.length;
    for (let i = 0; i < n; i++) {
        if (!team[i]) continue;
        while (j < n && (team[j] || i - j > dist)) j++;
        if (j < n && Math.abs(i - j) <= dist) {
            ans++;
            j++;
        }
    }
    return ans;
}
