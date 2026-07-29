// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

#include <stdlib.h>

typedef struct {
    int* times;
    int* leaders;
    int n;
} TopVotedCandidate;

TopVotedCandidate* topVotedCandidateCreate(int* persons, int personsSize, int* times, int timesSize) {
    (void)timesSize;
    TopVotedCandidate* obj = (TopVotedCandidate*)malloc(sizeof(TopVotedCandidate));
    obj->n = personsSize;
    obj->times = times;
    obj->leaders = (int*)malloc((size_t)personsSize * sizeof(int));
    int counts[5001] = {0};
    int leader = -1, leaderCount = 0;
    for (int i = 0; i < personsSize; i++) {
        int p = persons[i];
        counts[p]++;
        if (counts[p] >= leaderCount) {
            leader = p;
            leaderCount = counts[p];
        }
        obj->leaders[i] = leader;
    }
    return obj;
}

int topVotedCandidateQ(TopVotedCandidate* obj, int t) {
    int lo = 0, hi = obj->n - 1, ans = 0;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (obj->times[mid] <= t) {
            ans = mid;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    return obj->leaders[ans];
}

void topVotedCandidateFree(TopVotedCandidate* obj) {
    free(obj->leaders);
    free(obj);
}
