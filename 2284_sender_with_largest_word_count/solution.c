// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

#include <stdlib.h>
#include <string.h>

char* largestWordCount(char** messages, int messagesSize, char** senders, int sendersSize) {
    (void)sendersSize;
    char** names = (char**)malloc((size_t)messagesSize * sizeof(char*));
    int* counts = (int*)calloc((size_t)messagesSize, sizeof(int));
    int nNames = 0;
    char* best = senders[0];
    int bestCnt = -1;
    for (int i = 0; i < messagesSize; i++) {
        int words = 1;
        for (char* p = messages[i]; *p; p++) if (*p == ' ') words++;
        int idx = -1;
        for (int j = 0; j < nNames; j++) {
            if (strcmp(names[j], senders[i]) == 0) { idx = j; break; }
        }
        if (idx < 0) {
            idx = nNames++;
            names[idx] = senders[i];
        }
        counts[idx] += words;
        int c = counts[idx];
        if (c > bestCnt || (c == bestCnt && strcmp(senders[i], best) > 0)) {
            bestCnt = c;
            best = senders[i];
        }
    }
    free(names);
    free(counts);
    return best;
}
