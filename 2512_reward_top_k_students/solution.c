// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int id, score; } Pair2512;

static int cmp2512(const void* a, const void* b) {
    const Pair2512* x = a, *y = b;
    if (x->score != y->score) return y->score - x->score;
    return x->id - y->id;
}

static bool inSet(char** arr, int n, const char* w, int wlen) {
    for (int i = 0; i < n; i++) {
        if ((int)strlen(arr[i]) == wlen && strncmp(arr[i], w, (size_t)wlen) == 0) return true;
    }
    return false;
}

int* topStudents(char** positive_feedback, int positive_feedbackSize, char** negative_feedback, int negative_feedbackSize, char** report, int reportSize, int* student_id, int student_idSize, int k, int* returnSize) {
    (void)student_idSize;
    Pair2512* arr = (Pair2512*)malloc((size_t)reportSize * sizeof(Pair2512));
    for (int i = 0; i < reportSize; i++) {
        int score = 0;
        char* p = report[i];
        while (*p) {
            while (*p == ' ') p++;
            if (!*p) break;
            char* start = p;
            while (*p && *p != ' ') p++;
            int len = (int)(p - start);
            char tmp[32];
            if (len < 31) {
                memcpy(tmp, start, (size_t)len);
                tmp[len] = 0;
                if (inSet(positive_feedback, positive_feedbackSize, tmp, len)) score += 3;
                else if (inSet(negative_feedback, negative_feedbackSize, tmp, len)) score--;
            }
        }
        arr[i].id = student_id[i];
        arr[i].score = score;
    }
    qsort(arr, (size_t)reportSize, sizeof(Pair2512), cmp2512);
    int* ans = (int*)malloc((size_t)k * sizeof(int));
    for (int i = 0; i < k; i++) ans[i] = arr[i].id;
    free(arr);
    *returnSize = k;
    return ans;
}
