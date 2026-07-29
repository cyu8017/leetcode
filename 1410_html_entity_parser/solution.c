// LeetCode 1410 - HTML Entity Parser
// https://leetcode.com/problems/html-entity-parser/

#include <stdlib.h>
#include <string.h>

char* entityParser(char* text) {
    // Replace carefully: &amp; last among amp-containing - process sequentially like Python dict order
    // Python: quot, apos, amp, gt, lt, frasl - amp before would break if amp first; order matters
    const char* enc[] = {"&quot;", "&apos;", "&amp;", "&gt;", "&lt;", "&frasl;"};
    const char* dec[] = {"\"", "'", "&", ">", "<", "/"};
    char* cur = (char*)malloc(strlen(text) + 1);
    strcpy(cur, text);
    for (int e = 0; e < 6; e++) {
        size_t el = strlen(enc[e]), dl = strlen(dec[e]);
        size_t n = strlen(cur);
        char* nxt = (char*)malloc(n * 2 + 1);
        size_t j = 0;
        for (size_t i = 0; i < n; ) {
            if (strncmp(cur + i, enc[e], el) == 0) {
                memcpy(nxt + j, dec[e], dl);
                j += dl; i += el;
            } else nxt[j++] = cur[i++];
        }
        nxt[j] = '\0';
        free(cur);
        cur = nxt;
    }
    return cur;
}
