// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

int countLargestGroup(int n) {
    int cnt[40] = {0};
    for (int x = 1; x <= n; x++) {
        int s = 0, t = x;
        while (t) { s += t % 10; t /= 10; }
        cnt[s]++;
    }
    int mx = 0, ans = 0;
    for (int i = 0; i < 40; i++) if (cnt[i] > mx) mx = cnt[i];
    for (int i = 0; i < 40; i++) if (cnt[i] == mx) ans++;
    return ans;
}
