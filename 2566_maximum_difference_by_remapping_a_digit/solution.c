// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

static int remap2566(const char* s, int len, char from, char to) {
    int v = 0;
    for (int i = 0; i < len; i++) {
        char d = s[i];
        if (d == from) d = to;
        v = v * 10 + (d - '0');
    }
    return v;
}

int minMaxDifference(int num) {
    char s[16];
    int len = 0;
    int x = num;
    if (x == 0) s[len++] = '0';
    else {
        char tmp[16]; int tlen = 0;
        while (x > 0) { tmp[tlen++] = (char)('0' + x % 10); x /= 10; }
        for (int i = tlen - 1; i >= 0; i--) s[len++] = tmp[i];
    }
    int maxV = num;
    for (int i = 0; i < len; i++) {
        if (s[i] != '9') { maxV = remap2566(s, len, s[i], '9'); break; }
    }
    int minV = remap2566(s, len, s[0], '0');
    return maxV - minV;
}
