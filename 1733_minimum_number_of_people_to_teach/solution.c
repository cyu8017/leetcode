// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

#include <stdbool.h>
#include <stdlib.h>

int minimumTeachings(int n, int** languages, int languagesSize, int* languagesColSize,
                     int** friendships, int friendshipsSize, int* friendshipsColSize) {
    int users = languagesSize;
    bool* knows = (bool*)calloc((size_t)users * (n + 1), sizeof(bool));
    for (int user = 0; user < users; user++) {
        for (int i = 0; i < languagesColSize[user]; i++) {
            knows[user * (n + 1) + languages[user][i]] = true;
        }
    }
    bool* need = (bool*)calloc(users, sizeof(bool));
    for (int f = 0; f < friendshipsSize; f++) {
        int u = friendships[f][0] - 1;
        int v = friendships[f][1] - 1;
        bool shares = false;
        for (int i = 0; i < languagesColSize[u]; i++) {
            if (knows[v * (n + 1) + languages[u][i]]) {
                shares = true;
                break;
            }
        }
        if (!shares) {
            need[u] = true;
            need[v] = true;
        }
    }
    bool anyNeed = false;
    for (int user = 0; user < users; user++) {
        if (need[user]) {
            anyNeed = true;
            break;
        }
    }
    if (!anyNeed) {
        free(knows);
        free(need);
        return 0;
    }
    int best = users + 1;
    for (int lang = 1; lang <= n; lang++) {
        int teach = 0;
        for (int user = 0; user < users; user++) {
            if (need[user] && !knows[user * (n + 1) + lang]) teach++;
        }
        if (teach < best) {
            best = teach;
        }
    }
    free(knows);
    free(need);
    return best;
}
