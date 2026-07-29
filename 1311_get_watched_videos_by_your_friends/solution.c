// LeetCode 1311 - Get Watched Videos by Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { char* video; int count; } VC;

static int cmp_vc(const void* a, const void* b) {
    const VC* x = (const VC*)a;
    const VC* y = (const VC*)b;
    if (x->count != y->count) return x->count - y->count;
    return strcmp(x->video, y->video);
}

char** watchedVideosByFriends(char*** watchedVideos, int watchedVideosSize, int* watchedVideosColSize,
                              int** friends, int friendsSize, int* friendsColSize,
                              int id, int level, int* returnSize) {
    (void)watchedVideosSize; (void)friendsSize;
    bool* seen = (bool*)calloc(friendsSize, sizeof(bool));
    int* queue = (int*)malloc(friendsSize * sizeof(int));
    int* dist = (int*)malloc(friendsSize * sizeof(int));
    int qh = 0, qt = 0;
    queue[qt] = id; dist[qt++] = 0; seen[id] = true;
    int* people = (int*)malloc(friendsSize * sizeof(int));
    int peopleSize = 0;
    while (qh < qt) {
        int person = queue[qh];
        int distance = dist[qh++];
        if (distance == level) { people[peopleSize++] = person; continue; }
        for (int i = 0; i < friendsColSize[person]; i++) {
            int f = friends[person][i];
            if (!seen[f]) {
                seen[f] = true;
                queue[qt] = f; dist[qt++] = distance + 1;
            }
        }
    }
    VC* counts = (VC*)malloc(20000 * sizeof(VC));
    int cn = 0;
    for (int p = 0; p < peopleSize; p++) {
        int person = people[p];
        for (int i = 0; i < watchedVideosColSize[person]; i++) {
            char* v = watchedVideos[person][i];
            int found = -1;
            for (int j = 0; j < cn; j++) if (strcmp(counts[j].video, v) == 0) { found = j; break; }
            if (found >= 0) counts[found].count++;
            else { counts[cn].video = v; counts[cn].count = 1; cn++; }
        }
    }
    qsort(counts, cn, sizeof(VC), cmp_vc);
    char** ans = (char**)malloc(cn * sizeof(char*));
    for (int i = 0; i < cn; i++) {
        ans[i] = (char*)malloc(strlen(counts[i].video) + 1);
        strcpy(ans[i], counts[i].video);
    }
    free(seen); free(queue); free(dist); free(people); free(counts);
    *returnSize = cn;
    return ans;
}
