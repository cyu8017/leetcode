// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static void padNum(int x, char* out, int width) {
    char tmp[16]; sprintf(tmp, "%d", x);
    int len = (int)strlen(tmp);
    int pad = width - len;
    for (int i = 0; i < pad; i++) out[i] = '0';
    memcpy(out + pad, tmp, (size_t)len + 1);
}

static int dfsSwaps(char* bsa, const char* sb, int n, int start, int left) {
    if (strcmp(bsa, sb) == 0) return 1;
    if (left == 0) return 0;
    for (int i = start; i < n; i++) {
        if (bsa[i] == sb[i]) continue;
        for (int j = i + 1; j < n; j++) {
            if (bsa[j] == sb[i]) {
                char t = bsa[i]; bsa[i] = bsa[j]; bsa[j] = t;
                if (dfsSwaps(bsa, sb, n, i + 1, left - 1)) return 1;
                t = bsa[i]; bsa[i] = bsa[j]; bsa[j] = t;
            }
        }
        return 0;
    }
    return strcmp(bsa, sb) == 0;
}

static int almostEqual3267(int a, int b) {
    char ta[16], tb[16], sa[16], sb[16];
    sprintf(ta, "%d", a); sprintf(tb, "%d", b);
    int wa = (int)strlen(ta), wb = (int)strlen(tb);
    int w = wa > wb ? wa : wb;
    padNum(a, sa, w); padNum(b, sb, w);
    if (strcmp(sa, sb) == 0) return 1;
    char bsa[16]; memcpy(bsa, sa, (size_t)w + 1);
    return dfsSwaps(bsa, sb, w, 0, 2);
}

int countPairs(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++)
        for (int j = i + 1; j < numsSize; j++)
            if (almostEqual3267(nums[i], nums[j])) ans++;
    return ans;
}
