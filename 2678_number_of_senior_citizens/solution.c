// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

int countSeniors(char** details, int detailsSize) {
    int ans = 0;
    for (int i = 0; i < detailsSize; i++) {
        int age = (details[i][11] - '0') * 10 + (details[i][12] - '0');
        if (age > 60) ans++;
    }
    return ans;
}
