// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int cmpMeet(const void* a, const void* b) {
    int* const* ma = (int* const*)a;
    int* const* mb = (int* const*)b;
    return (*ma)[2] - (*mb)[2];
}

static int find2092(int* parent, int x) {
    if (parent[x] != x) parent[x] = find2092(parent, parent[x]);
    return parent[x];
}

static void uni2092(int* parent, int a, int b) {
    int ra = find2092(parent, a), rb = find2092(parent, b);
    if (ra != rb) parent[ra] = rb;
}

int* findAllPeople(int n, int** meetings, int meetingsSize, int* meetingsColSize, int firstPerson, int* returnSize) {
    (void)meetingsColSize;
    qsort(meetings, (size_t)meetingsSize, sizeof(int*), cmpMeet);
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    bool* know = (bool*)calloc((size_t)n, sizeof(bool));
    know[0] = know[firstPerson] = true;
    uni2092(parent, 0, firstPerson);
    for (int i = 0; i < meetingsSize; ) {
        int j = i;
        while (j < meetingsSize && meetings[j][2] == meetings[i][2]) j++;
        for (int k = i; k < j; k++) uni2092(parent, meetings[k][0], meetings[k][1]);
        int root0 = find2092(parent, 0);
        int* reset = (int*)malloc((size_t)(j - i) * 2 * sizeof(int));
        int rn = 0;
        for (int k = i; k < j; k++) {
            int a = meetings[k][0], b = meetings[k][1];
            if (find2092(parent, a) != root0) { reset[rn++] = a; reset[rn++] = b; }
            else { know[a] = know[b] = true; }
        }
        for (int k = 0; k < rn; k++) parent[reset[k]] = reset[k];
        free(reset);
        i = j;
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int an = 0;
    int root0 = find2092(parent, 0);
    for (int i = 0; i < n; i++) if (find2092(parent, i) == root0 || know[i]) ans[an++] = i;
    free(parent); free(know);
    *returnSize = an;
    return ans;
}
