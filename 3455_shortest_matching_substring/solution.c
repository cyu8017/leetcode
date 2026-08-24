// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

#include <stdlib.h>
#include <string.h>

static int sortSearch(int* arr, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (arr[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

static int* findAll(const char* s, int n, const char* sub, int subLen, int* outCount) {
    if (subLen == 0) {
        int* res = (int*)malloc((size_t)(n + 1) * sizeof(int));
        for (int i = 0; i <= n; i++) res[i] = i;
        *outCount = n + 1;
        return res;
    }
    int cap = 16, cnt = 0;
    int* res = (int*)malloc((size_t)cap * sizeof(int));
    for (int i = 0; i + subLen <= n; i++) {
        if (strncmp(s + i, sub, (size_t)subLen) == 0) {
            if (cnt == cap) {
                cap *= 2;
                res = (int*)realloc(res, (size_t)cap * sizeof(int));
            }
            res[cnt++] = i;
        }
    }
    *outCount = cnt;
    return res;
}

int shortestMatchingSubstring(char* s, char* p) {
    int n = (int)strlen(s);
    char* pcopy = strdup(p);
    char* parts[3] = {"", "", ""};
    int pc = 0;
    char* tok = strtok(pcopy, "*");
    char* start = pcopy;
    /* Handle leading/empty splits carefully */
    free(pcopy);
    /* Manual split on '*' ensuring 3 parts */
    int plen = (int)strlen(p);
    char* a = (char*)calloc((size_t)plen + 1, 1);
    char* b = (char*)calloc((size_t)plen + 1, 1);
    char* c = (char*)calloc((size_t)plen + 1, 1);
    int stars = 0, ai = 0, bi = 0, ci = 0;
    for (int i = 0; i < plen; i++) {
        if (p[i] == '*') {
            stars++;
            continue;
        }
        if (stars == 0) a[ai++] = p[i];
        else if (stars == 1) b[bi++] = p[i];
        else c[ci++] = p[i];
    }
    int al = ai, bl = bi, cl = ci;
    int na, nb, nc;
    int* posA = findAll(s, n, a, al, &na);
    int* posB = findAll(s, n, b, bl, &nb);
    int* posC = findAll(s, n, c, cl, &nc);
    int ans = n + 1;
    for (int iax = 0; iax < na; iax++) {
        int ia = posA[iax];
        int endA = ia + al;
        int bi2 = sortSearch(posB, nb, endA);
        for (; bi2 < nb; bi2++) {
            int endB = posB[bi2] + bl;
            int ci2 = sortSearch(posC, nc, endB);
            if (ci2 < nc) {
                int length = posC[ci2] + cl - ia;
                if (length < ans) ans = length;
            }
            break;
        }
    }
    free(a); free(b); free(c);
    free(posA); free(posB); free(posC);
    return ans == n + 1 ? -1 : ans;
}
