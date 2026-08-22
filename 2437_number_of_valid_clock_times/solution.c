// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

int countTime(char* time) {
    int ans = 0;
    for (int h = 0; h < 24; h++) {
        for (int m = 0; m < 60; m++) {
            char hs0 = (char)('0' + h / 10), hs1 = (char)('0' + h % 10);
            char ms0 = (char)('0' + m / 10), ms1 = (char)('0' + m % 10);
            if (time[0] != '?' && time[0] != hs0) continue;
            if (time[1] != '?' && time[1] != hs1) continue;
            if (time[3] != '?' && time[3] != ms0) continue;
            if (time[4] != '?' && time[4] != ms1) continue;
            ans++;
        }
    }
    return ans;
}
