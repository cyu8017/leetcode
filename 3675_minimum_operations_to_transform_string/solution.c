// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

int minOperations(char* s) {
    int ans = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] != 'a') {
            int v = 26 - (s[i] - 'a');
            if (v > ans) ans = v;
        }
    }
    return ans;
}
