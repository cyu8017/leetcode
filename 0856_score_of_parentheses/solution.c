// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

int scoreOfParentheses(char* s) {
    int stack[50], top = 0;
    stack[top++] = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '(') stack[top++] = 0;
        else {
            int v = stack[--top];
            int add = v == 0 ? 1 : 2 * v;
            stack[top - 1] += add;
        }
    }
    return stack[0];
}
