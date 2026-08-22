// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

#include <stdlib.h>

static int searchPrefix(long long* prefix, int j, long long threshold) {
    /* sort.Search(j, func(i int) bool { return prefix[i] >= threshold }) */
    int lo = 0, hi = j;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (prefix[mid] >= threshold) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

long long totalScore(int hp, int* damage, int damageSize, int* requirement, int requirementSize) {
    (void)requirementSize;
    int n = damageSize;
    long long* prefix = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + damage[i];
    long long answer = (long long)n * (n + 1) / 2;
    for (int j = 1; j <= n; j++) {
        long long threshold = prefix[j] + (long long)(requirement[j - 1] - hp);
        int invalid = searchPrefix(prefix, j, threshold);
        answer -= invalid;
    }
    free(prefix);
    return answer;
}
