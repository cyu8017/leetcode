// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

#include <stdbool.h>
#include <string.h>

bool parseBoolExpr(char* expression) {
    char stack[20005];
    int top = 0;
    for (char* p = expression; *p; p++) {
        char ch = *p;
        if (ch == ')') {
            bool values[20005];
            int vcount = 0;
            while (top > 0 && stack[top - 1] != '&' && stack[top - 1] != '|' && stack[top - 1] != '!') {
                char token = stack[--top];
                if (token == 't' || token == 'f') values[vcount++] = (token == 't');
            }
            char op = stack[--top];
            bool res;
            if (op == '!') {
                res = !values[0];
            } else if (op == '&') {
                res = true;
                for (int i = 0; i < vcount; i++) if (!values[i]) { res = false; break; }
            } else {
                res = false;
                for (int i = 0; i < vcount; i++) if (values[i]) { res = true; break; }
            }
            stack[top++] = res ? 't' : 'f';
        } else if (ch != ',') {
            stack[top++] = ch;
        }
    }
    return stack[top - 1] == 't';
}
