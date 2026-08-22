// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

#include <stdlib.h>
#include <string.h>

typedef struct { char* name; int* times; int tn, tcap; } Emp;

static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }
static int cmp_str(const void* a, const void* b) { return strcmp(*(char* const*)a, *(char* const*)b); }

char** findHighAccessEmployees(char*** accessTimes, int accessTimesSize, int* accessTimesColSize, int* returnSize) {
    (void)accessTimesColSize;
    Emp* emps = (Emp*)calloc(accessTimesSize, sizeof(Emp));
    int en = 0;
    for (int i = 0; i < accessTimesSize; i++) {
        char* name = accessTimes[i][0];
        char* t = accessTimes[i][1];
        int mins = (t[0]-'0')*600 + (t[1]-'0')*60 + (t[2]-'0')*10 + (t[3]-'0');
        int found = -1;
        for (int j = 0; j < en; j++) if (strcmp(emps[j].name, name) == 0) { found = j; break; }
        if (found < 0) {
            found = en++;
            emps[found].name = name;
            emps[found].tcap = 4;
            emps[found].times = (int*)malloc(4 * sizeof(int));
            emps[found].tn = 0;
        }
        if (emps[found].tn == emps[found].tcap) {
            emps[found].tcap *= 2;
            emps[found].times = (int*)realloc(emps[found].times, emps[found].tcap * sizeof(int));
        }
        emps[found].times[emps[found].tn++] = mins;
    }
    char** ans = (char**)malloc(en * sizeof(char*));
    int an = 0;
    for (int i = 0; i < en; i++) {
        qsort(emps[i].times, emps[i].tn, sizeof(int), cmp_int);
        for (int j = 0; j + 2 < emps[i].tn; j++) {
            if (emps[i].times[j + 2] - emps[i].times[j] < 60) {
                ans[an++] = emps[i].name;
                break;
            }
        }
        free(emps[i].times);
    }
    free(emps);
    qsort(ans, an, sizeof(char*), cmp_str);
    *returnSize = an;
    return ans;
}
