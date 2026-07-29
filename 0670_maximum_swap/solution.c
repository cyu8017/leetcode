// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

int maximumSwap(int num) {
    char s[16];
    int n = 0;
    int x = num;
    if (x == 0) return 0;
    char tmp[16];
    int t = 0;
    while (x) { tmp[t++] = (char)('0' + x % 10); x /= 10; }
    for (int i = t - 1; i >= 0; i--) s[n++] = tmp[i];
    s[n] = '\0';
    int last[10];
    for (int i = 0; i < 10; i++) last[i] = -1;
    for (int i = 0; i < n; i++) last[s[i] - '0'] = i;
    for (int i = 0; i < n; i++) {
        for (int d = 9; d > s[i] - '0'; d--) {
            if (last[d] > i) {
                char c = s[i]; s[i] = s[last[d]]; s[last[d]] = c;
                int ans = 0;
                for (int j = 0; j < n; j++) ans = ans * 10 + (s[j] - '0');
                return ans;
            }
        }
    }
    return num;
}
