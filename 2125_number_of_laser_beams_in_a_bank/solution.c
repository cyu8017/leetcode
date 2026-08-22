// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

int numberOfBeams(char** bank, int bankSize) {
    int ans = 0, prev = 0;
    for (int i = 0; i < bankSize; i++) {
        int cnt = 0;
        for (char* p = bank[i]; *p; p++) if (*p == '1') cnt++;
        if (cnt > 0) { ans += prev * cnt; prev = cnt; }
    }
    return ans;
}
