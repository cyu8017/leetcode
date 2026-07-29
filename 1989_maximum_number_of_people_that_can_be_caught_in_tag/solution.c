// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

int catchMaximumAmountofPeople(int* team, int teamSize, int dist) {
    int ans = 0;
    int j = 0;
    for (int i = 0; i < teamSize; i++) {
        if (team[i] != 1) continue;
        while (j < teamSize && (j < i - dist || team[j] != 0)) j++;
        if (j < teamSize && j <= i + dist) {
            ans++;
            j++;
        }
    }
    return ans;
}
