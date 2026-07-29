// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

static int toMin(char* t) {
    return (t[0] - '0') * 600 + (t[1] - '0') * 60 + (t[3] - '0') * 10 + (t[4] - '0');
}

int numberOfRounds(char* loginTime, char* logoutTime) {
    int start = toMin(loginTime);
    int end = toMin(logoutTime);
    if (end < start) end += 24 * 60;
    start = (start + 14) / 15 * 15;
    end = end / 15 * 15;
    int diff = (end - start) / 15;
    return diff > 0 ? diff : 0;
}
