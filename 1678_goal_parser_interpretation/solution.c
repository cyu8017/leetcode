// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

#include <stdlib.h>
#include <string.h>

char* interpret(char* command) {
    int n = (int)strlen(command);
    char* out = (char*)malloc((size_t)n + 1);
    int j = 0;
    for (int i = 0; command[i]; ) {
        if (command[i] == 'G') { out[j++] = 'G'; i++; }
        else if (command[i] == '(' && command[i + 1] == ')') { out[j++] = 'o'; i += 2; }
        else { out[j++] = 'a'; out[j++] = 'l'; i += 4; }
    }
    out[j] = '\0';
    return out;
}
