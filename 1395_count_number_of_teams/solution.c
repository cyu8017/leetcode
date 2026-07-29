// LeetCode 1395 - Count Number of Teams
// https://leetcode.com/problems/count-number-of-teams/

int numTeams(int* rating, int ratingSize) {
    int ans = 0;
    for (int j = 0; j < ratingSize; j++) {
        int ll = 0, lg = 0, rl = 0, rg = 0;
        for (int i = 0; i < j; i++) {
            if (rating[i] < rating[j]) ll++;
            else lg++;
        }
        for (int i = j + 1; i < ratingSize; i++) {
            if (rating[i] > rating[j]) rg++;
            else rl++;
        }
        ans += ll * rg + lg * rl;
    }
    return ans;
}
