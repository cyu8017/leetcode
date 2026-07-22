// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

int maxDepth(char* s) {
    int depth = 0, ans = 0;
    for (; *s; s++) {
        if (*s == '(') {
            depth++;
            if (depth > ans) ans = depth;
        } else if (*s == ')') {
            depth--;
        }
    }
    return ans;
}
