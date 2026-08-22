// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

int findWinningPlayer(int* skills, int skillsSize, int k) {
    int n = skillsSize;
    if (k > n - 1) k = n - 1;
    int i = 0, cnt = 0;
    for (int j = 1; j < n; j++) {
        if (skills[i] < skills[j]) { i = j; cnt = 1; }
        else cnt++;
        if (cnt == k) break;
    }
    return i;
}
