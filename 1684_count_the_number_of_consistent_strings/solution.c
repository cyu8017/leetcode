// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

int countConsistentStrings(char* allowed, char** words, int wordsSize) {
    int mask = 0;
    for (char* p = allowed; *p; p++) mask |= 1 << (*p - 'a');
    int ans = 0;
    for (int i = 0; i < wordsSize; i++) {
        int ok = 1;
        for (char* p = words[i]; *p; p++) {
            if (!(mask & (1 << (*p - 'a')))) { ok = 0; break; }
        }
        ans += ok;
    }
    return ans;
}
