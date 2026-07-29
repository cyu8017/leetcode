// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

int maximum69Number (int num) {
    char buf[16];
    int n = 0, x = num;
    char tmp[16];
    if (x == 0) { buf[0] = '0'; n = 1; }
    else {
        while (x) { tmp[n++] = '0' + (x % 10); x /= 10; }
        for (int i = 0; i < n; i++) buf[i] = tmp[n - 1 - i];
    }
    buf[n] = 0;
    for (int i = 0; i < n; i++) if (buf[i] == '6') { buf[i] = '9'; break; }
    int ans = 0;
    for (int i = 0; i < n; i++) ans = ans * 10 + (buf[i] - '0');
    return ans;
}
