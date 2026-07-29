// LeetCode 0752 - Open the Lock
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int openLock(char** deadends, int deadendsSize, char* target) {
    bool dead[10000] = {0}, seen[10000] = {0};
    for (int i = 0; i < deadendsSize; i++) dead[atoi(deadends[i])] = true;
    if (dead[0]) return -1;
    int* q = (int*)malloc(10000 * sizeof(int));
    int* dist = (int*)malloc(10000 * sizeof(int));
    int head = 0, tail = 0;
    q[tail] = 0; dist[tail++] = 0; seen[0] = true;
    int t = atoi(target);
    while (head < tail) {
        int state = q[head], steps = dist[head]; head++;
        if (state == t) { free(q); free(dist); return steps; }
        int digits[4] = {state/1000, (state/100)%10, (state/10)%10, state%10};
        for (int i = 0; i < 4; i++) {
            for (int d = -1; d <= 1; d += 2) {
                int nd[4]; memcpy(nd, digits, sizeof(digits));
                nd[i] = (nd[i] + d + 10) % 10;
                int nxt = nd[0]*1000 + nd[1]*100 + nd[2]*10 + nd[3];
                if (!seen[nxt] && !dead[nxt]) { seen[nxt]=true; q[tail]=nxt; dist[tail++]=steps+1; }
            }
        }
    }
    free(q); free(dist); return -1;
}
