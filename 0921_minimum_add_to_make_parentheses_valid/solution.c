// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

int minAddToMakeValid(char* s) {
    int openNeed = 0, closeNeed = 0;
    for (; *s; s++) {
        if (*s == '(') {
            closeNeed++;
        } else if (closeNeed) {
            closeNeed--;
        } else {
            openNeed++;
        }
    }
    return openNeed + closeNeed;
}
