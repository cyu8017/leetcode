// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

int divisorSubstrings(int num, int k) {
    char s[32];
    int n = 0, t = num;
    if (t == 0) s[n++] = '0';
    else {
        char tmp[32];
        int m = 0;
        while (t > 0) { tmp[m++] = (char)('0' + t % 10); t /= 10; }
        for (int i = m - 1; i >= 0; i--) s[n++] = tmp[i];
    }
    s[n] = '\0';
    int ans = 0;
    for (int i = 0; i + k <= n; i++) {
        int sub = 0;
        for (int j = 0; j < k; j++) sub = sub * 10 + (s[i + j] - '0');
        if (sub != 0 && num % sub == 0) ans++;
    }
    return ans;
}
