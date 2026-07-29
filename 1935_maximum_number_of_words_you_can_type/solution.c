// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

int canBeTypedWords(char* text, char* brokenLetters) {
    int broken[26] = {0};
    for (char* p = brokenLetters; *p; p++) broken[*p - 'a'] = 1;
    int ans = 0;
    int ok = 1;
    for (char* p = text; ; p++) {
        if (*p == ' ' || *p == '\0') {
            if (ok) ans++;
            ok = 1;
            if (*p == '\0') break;
        } else if (broken[*p - 'a']) {
            ok = 0;
        }
    }
    return ans;
}
