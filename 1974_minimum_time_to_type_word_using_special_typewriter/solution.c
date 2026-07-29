// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

int minTimeToType(char* word) {
    int ans = 0;
    char prev = 'a';
    for (char* p = word; *p; p++) {
        int diff = *p - prev;
        if (diff < 0) diff = -diff;
        int other = 26 - diff;
        ans += (diff < other ? diff : other) + 1;
        prev = *p;
    }
    return ans;
}
