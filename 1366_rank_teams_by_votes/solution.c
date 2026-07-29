// LeetCode 1366 - Rank Teams by Votes
// https://leetcode.com/problems/rank-teams-by-votes/

#include <stdlib.h>
#include <string.h>

char* rankTeams(char** votes, int votesSize) {
    int m = (int)strlen(votes[0]);
    int count[26][26] = {{0}};
    int present[26] = {0};
    for (int i = 0; i < m; i++) present[votes[0][i] - 'A'] = 1;
    for (int v = 0; v < votesSize; v++)
        for (int i = 0; i < m; i++) count[votes[v][i] - 'A'][i]++;
    char* teams = (char*)malloc(m + 1);
    int tn = 0;
    for (int c = 0; c < 26; c++) if (present[c]) teams[tn++] = 'A' + c;
    teams[tn] = '\0';
    for (int i = 0; i < tn; i++) {
        for (int j = i + 1; j < tn; j++) {
            int ca = teams[i] - 'A', cb = teams[j] - 'A';
            int better = 0;
            for (int k = 0; k < m; k++) {
                if (count[ca][k] != count[cb][k]) {
                    better = count[ca][k] > count[cb][k] ? 1 : -1;
                    break;
                }
            }
            if (better < 0 || (better == 0 && teams[i] > teams[j])) {
                char t = teams[i]; teams[i] = teams[j]; teams[j] = t;
            }
        }
    }
    return teams;
}
