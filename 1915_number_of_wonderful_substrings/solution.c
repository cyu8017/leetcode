// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

long long wonderfulSubstrings(char* word) {
    int count[1024] = {0};
    count[0] = 1;
    int mask = 0;
    long long ans = 0;
    for (char* p = word; *p; p++) {
        mask ^= 1 << (*p - 'a');
        ans += count[mask];
        for (int bit = 0; bit < 10; bit++) ans += count[mask ^ (1 << bit)];
        count[mask]++;
    }
    return ans;
}
