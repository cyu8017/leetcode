// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

#include <stdlib.h>
#include <string.h>

static int findParent(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unite(int* parent, int a, int b) {
    int ra = findParent(parent, a);
    int rb = findParent(parent, b);
    if (ra == rb) {
        return;
    }
    if (ra < rb) {
        parent[rb] = ra;
    } else {
        parent[ra] = rb;
    }
}

char* smallestEquivalentString(char* s1, char* s2, char* baseStr) {
    int parent[26];
    for (int i = 0; i < 26; i++) {
        parent[i] = i;
    }
    for (int i = 0; s1[i]; i++) {
        unite(parent, s1[i] - 'a', s2[i] - 'a');
    }
    int n = (int)strlen(baseStr);
    char* ans = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) {
        ans[i] = (char)('a' + findParent(parent, baseStr[i] - 'a'));
    }
    ans[n] = '\0';
    return ans;
}
