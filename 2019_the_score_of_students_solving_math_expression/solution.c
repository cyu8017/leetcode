// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int evalCorrect2019(const char* s) {
    int nums[64], nn = 0;
    char ops[64]; int on = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] >= '0' && s[i] <= '9') nums[nn++] = s[i] - '0';
        else ops[on++] = s[i];
    }
    int newNums[64], nnn = 0;
    char newOps[64]; int non = 0;
    newNums[nnn++] = nums[0];
    for (int j = 0; j < on; j++) {
        if (ops[j] == '*') newNums[nnn - 1] *= nums[j + 1];
        else { newOps[non++] = ops[j]; newNums[nnn++] = nums[j + 1]; }
    }
    int res = newNums[0];
    for (int j = 0; j < non; j++) res += newNums[j + 1];
    return res;
}

typedef struct { int* vals; int n; int cap; bool ready; } Set2019;

static void setAdd(Set2019* st, int v) {
    for (int i = 0; i < st->n; i++) if (st->vals[i] == v) return;
    if (st->n == st->cap) {
        st->cap = st->cap ? st->cap * 2 : 8;
        st->vals = (int*)realloc(st->vals, (size_t)st->cap * sizeof(int));
    }
    st->vals[st->n++] = v;
}

static Set2019* dp2019;
static int N2019;
static const char* S2019;

static Set2019* dfs2019(int l, int r) {
    Set2019* cell = &dp2019[l * N2019 + r];
    if (cell->ready) return cell;
    cell->ready = true;
    if (l == r) { setAdd(cell, S2019[l] - '0'); return cell; }
    for (int i = l + 1; i < r; i += 2) {
        Set2019* left = dfs2019(l, i - 1);
        Set2019* right = dfs2019(i + 1, r);
        for (int a = 0; a < left->n; a++) {
            for (int b = 0; b < right->n; b++) {
                int v = S2019[i] == '+' ? left->vals[a] + right->vals[b] : left->vals[a] * right->vals[b];
                if (v <= 1000) setAdd(cell, v);
            }
        }
    }
    return cell;
}

int scoreOfStudents(char* s, int* answers, int answersSize) {
    N2019 = (int)strlen(s);
    S2019 = s;
    dp2019 = (Set2019*)calloc((size_t)N2019 * N2019, sizeof(Set2019));
    int correct = evalCorrect2019(s);
    Set2019* possible = dfs2019(0, N2019 - 1);
    bool ok[1001] = {0};
    for (int i = 0; i < possible->n; i++) if (possible->vals[i] >= 0 && possible->vals[i] <= 1000) ok[possible->vals[i]] = true;
    int ans = 0;
    for (int i = 0; i < answersSize; i++) {
        if (answers[i] == correct) ans += 5;
        else if (answers[i] >= 0 && answers[i] <= 1000 && ok[answers[i]]) ans += 2;
    }
    for (int i = 0; i < N2019 * N2019; i++) free(dp2019[i].vals);
    free(dp2019);
    return ans;
}
