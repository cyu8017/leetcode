// LeetCode 1358 - Number of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

int numberOfSubstrings(char* s) {
    int last[3] = {-1, -1, -1};
    int ans = 0;
    for (int i = 0; s[i]; i++) {
        last[s[i] - 'a'] = i;
        int m = last[0];
        if (last[1] < m) m = last[1];
        if (last[2] < m) m = last[2];
        ans += m + 1;
    }
    return ans;
}
