// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

int minInsertions(char* s) {
    int insertions = 0, needed = 0;
    for (; *s; s++) {
        if (*s == '(') {
            needed += 2;
            if (needed & 1) {
                insertions++;
                needed--;
            }
        } else {
            needed--;
            if (needed < 0) {
                insertions++;
                needed = 1;
            }
        }
    }
    return insertions + needed;
}
