// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

#include <stdlib.h>

typedef struct { int sid, used; } Stu;
typedef struct { int bench; Stu* s; int n, cap; int used; } Bench;

int maxStudentsOnBench(int** students, int studentsSize, int* studentsColSize) {
    (void)studentsColSize;
    /* simple O(n^2) unique count per bench */
    int* benches = (int*)malloc(studentsSize * sizeof(int));
    int bn = 0;
    for (int i = 0; i < studentsSize; i++) {
        int b = students[i][1], found = 0;
        for (int j = 0; j < bn; j++) if (benches[j] == b) { found = 1; break; }
        if (!found) benches[bn++] = b;
    }
    int ans = 0;
    for (int bi = 0; bi < bn; bi++) {
        int* ids = (int*)malloc(studentsSize * sizeof(int));
        int in = 0;
        for (int i = 0; i < studentsSize; i++) if (students[i][1] == benches[bi]) {
            int sid = students[i][0], found = 0;
            for (int j = 0; j < in; j++) if (ids[j] == sid) { found = 1; break; }
            if (!found) ids[in++] = sid;
        }
        if (in > ans) ans = in;
        free(ids);
    }
    free(benches);
    return ans;
}
