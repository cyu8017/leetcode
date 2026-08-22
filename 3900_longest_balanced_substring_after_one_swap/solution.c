// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

#include <stdlib.h>
#include <string.h>

/* map pre -> list of indices; pre ranges roughly -n..n, offset by n+1 */
int longestBalanced(char* s) {
    int n = (int)strlen(s);
    int cnt0 = 0;
    for (int i = 0; i < n; i++) if (s[i] == '0') cnt0++;
    int cnt1 = n - cnt0;
    int offset = n + 2;
    int range = 2 * n + 5;
    int** pos = calloc((size_t)range, sizeof(int*));
    int* psz = calloc((size_t)range, sizeof(int));
    int* pcap = calloc((size_t)range, sizeof(int));
    #define APPEND(pre, idx) do { \
        int __k = (pre) + offset; \
        if (psz[__k] == pcap[__k]) { \
            pcap[__k] = pcap[__k] ? pcap[__k] * 2 : 4; \
            pos[__k] = realloc(pos[__k], (size_t)pcap[__k] * sizeof(int)); \
        } \
        pos[__k][psz[__k]++] = (idx); \
    } while (0)
    APPEND(0, -1);
    int ans = 0, pre = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') pre++; else pre--;
        APPEND(pre, i);
        int k = pre + offset;
        if (i - pos[k][0] > ans) ans = i - pos[k][0];
        int k2 = pre - 2 + offset;
        if (k2 >= 0 && k2 < range && psz[k2] > 0) {
            if ((i - pos[k2][0] - 2) / 2 < cnt0) {
                if (i - pos[k2][0] > ans) ans = i - pos[k2][0];
            } else if (psz[k2] > 1) {
                if (i - pos[k2][1] > ans) ans = i - pos[k2][1];
            }
        }
        k2 = pre + 2 + offset;
        if (k2 >= 0 && k2 < range && psz[k2] > 0) {
            if ((i - pos[k2][0] - 2) / 2 < cnt1) {
                if (i - pos[k2][0] > ans) ans = i - pos[k2][0];
            } else if (psz[k2] > 1) {
                if (i - pos[k2][1] > ans) ans = i - pos[k2][1];
            }
        }
    }
    for (int i = 0; i < range; i++) free(pos[i]);
    free(pos); free(psz); free(pcap);
    return ans;
}
