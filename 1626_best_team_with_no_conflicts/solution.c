// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

#include <stdlib.h>

typedef struct { int age; int score; } Player;

static int cmpPlayer(const void* a, const void* b) {
    const Player* x = a, * y = b;
    if (x->age != y->age) return x->age - y->age;
    return x->score - y->score;
}

int bestTeamScore(int* scores, int scoresSize, int* ages, int agesSize) {
    (void)agesSize;
    Player* players = (Player*)malloc((size_t)scoresSize * sizeof(Player));
    for (int i = 0; i < scoresSize; i++) {
        players[i].age = ages[i];
        players[i].score = scores[i];
    }
    qsort(players, (size_t)scoresSize, sizeof(Player), cmpPlayer);
    int* dp = (int*)malloc((size_t)scoresSize * sizeof(int));
    int ans = 0;
    for (int i = 0; i < scoresSize; i++) {
        dp[i] = players[i].score;
        for (int j = 0; j < i; j++) {
            if (players[j].score <= players[i].score && dp[j] + players[i].score > dp[i]) {
                dp[i] = dp[j] + players[i].score;
            }
        }
        if (dp[i] > ans) ans = dp[i];
    }
    free(players); free(dp);
    return ans;
}
