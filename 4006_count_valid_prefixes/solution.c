// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

int countValidPrefixes(char* s) {
    int ans = 0, t = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '1') t++;
        else t--;
        if (t >= -1 && t <= 1) ans++;
    }
    return ans;
}
