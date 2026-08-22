// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

static int toMin(char* t) {
    return (t[0] - '0') * 600 + (t[1] - '0') * 60 + (t[3] - '0') * 10 + (t[4] - '0');
}

int convertTime(char* current, char* correct) {
    int diff = toMin(correct) - toMin(current);
    int ans = 0;
    int steps[] = {60, 15, 5, 1};
    for (int i = 0; i < 4; i++) {
        ans += diff / steps[i];
        diff %= steps[i];
    }
    return ans;
}
