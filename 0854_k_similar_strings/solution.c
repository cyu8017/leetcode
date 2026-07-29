// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { char* s; int dist; } QNode;

static unsigned hash_str(const char* s) {
    unsigned h = 2166136261u;
    for (const char* p = s; *p; p++) { h ^= (unsigned char)*p; h *= 16777619u; }
    return h;
}

int kSimilarity(char* s1, char* s2) {
    if (strcmp(s1, s2) == 0) return 0;
    int n = (int)strlen(s1);
    int qcap = 1 << 16;
    QNode* q = (QNode*)malloc((size_t)qcap * sizeof(QNode));
    int qh = 0, qt = 0;
    int scap = 1 << 17;
    char** slots = (char**)calloc((size_t)scap, sizeof(char*));

    char* start = (char*)malloc((size_t)n + 1);
    strcpy(start, s1);
    q[qt++] = (QNode){start, 0};
    {
        unsigned h = hash_str(start) & (scap - 1);
        while (slots[h]) h = (h + 1) & (scap - 1);
        slots[h] = start;
    }

    while (qh < qt) {
        QNode cur = q[qh++];
        char* arr = cur.s;
        int i = 0;
        while (arr[i] == s2[i]) i++;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] == s2[i] && arr[j] != s2[j]) {
                char* nxt = (char*)malloc((size_t)n + 1);
                strcpy(nxt, arr);
                char tmp = nxt[i]; nxt[i] = nxt[j]; nxt[j] = tmp;
                if (strcmp(nxt, s2) == 0) {
                    free(nxt);
                    return cur.dist + 1;
                }
                unsigned h = hash_str(nxt) & (scap - 1);
                bool found = false;
                while (slots[h]) {
                    if (strcmp(slots[h], nxt) == 0) { found = true; break; }
                    h = (h + 1) & (scap - 1);
                }
                if (!found) {
                    slots[h] = nxt;
                    if (qt == qcap) {
                        qcap *= 2;
                        q = (QNode*)realloc(q, (size_t)qcap * sizeof(QNode));
                    }
                    q[qt++] = (QNode){nxt, cur.dist + 1};
                } else free(nxt);
            }
        }
    }
    return -1;
}
