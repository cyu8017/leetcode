// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static char* build_match(const char* left, const char* right) {
    const int length = (int)strlen(left) + (int)strlen(right) + 3;
    char* match = (char*)malloc((size_t)length + 1);
    sprintf(match, "(%s,%s)", left, right);
    return match;
}

char* findContestMatch(int n) {
    char** teams = (char**)malloc((size_t)n * sizeof(char*));
    int teamCount = n;
    for (int team = 1; team <= n; team++) {
        teams[team - 1] = (char*)malloc(16);
        sprintf(teams[team - 1], "%d", team);
    }

    while (teamCount > 1) {
        const int nextCount = teamCount / 2;
        char** nextRound = (char**)malloc((size_t)nextCount * sizeof(char*));
        for (int index = 0; index < nextCount; index++) {
            nextRound[index] = build_match(teams[index], teams[teamCount - 1 - index]);
            free(teams[index]);
            free(teams[teamCount - 1 - index]);
        }
        free(teams);
        teams = nextRound;
        teamCount = nextCount;
    }

    char* result = teams[0];
    free(teams);
    return result;
}
