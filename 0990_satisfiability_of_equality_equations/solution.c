// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

#include <stdbool.h>

static int find(int* p, int x) {
    while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}

bool equationsPossible(char** equations, int equationsSize) {
    int parent[26];
    for (int i = 0; i < 26; i++) parent[i] = i;
    for (int i = 0; i < equationsSize; i++) {
        if (equations[i][1] == '=')
            parent[find(parent, equations[i][0] - 'a')] = find(parent, equations[i][3] - 'a');
    }
    for (int i = 0; i < equationsSize; i++) {
        if (equations[i][1] == '!' && find(parent, equations[i][0] - 'a') == find(parent, equations[i][3] - 'a'))
            return false;
    }
    return true;
}
