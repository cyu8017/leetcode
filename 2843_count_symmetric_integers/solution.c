// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

int countSymmetricIntegers(int low, int high) {
    int ans = 0;
    for (int x = low; x <= high; x++) {
        char s[16];
        int len = 0, t = x;
        if (t == 0) s[len++] = '0';
        else {
            char tmp[16]; int tl = 0;
            while (t) { tmp[tl++] = (char)('0' + t % 10); t /= 10; }
            for (int i = tl - 1; i >= 0; i--) s[len++] = tmp[i];
        }
        if (len % 2) continue;
        int mid = len / 2, a = 0, b = 0;
        for (int i = 0; i < mid; i++) {
            a += s[i] - '0';
            b += s[mid + i] - '0';
        }
        if (a == b) ans++;
    }
    return ans;
}
