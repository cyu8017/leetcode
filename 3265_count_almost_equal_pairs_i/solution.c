// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static void toStrPad(int x, char* buf, int width) {
    char tmp[16];
    sprintf(tmp, "%d", x);
    int len = (int)strlen(tmp);
    int pad = width - len;
    for (int i = 0; i < pad; i++) buf[i] = '0';
    memcpy(buf + pad, tmp, (size_t)len + 1);
}

static int almostEqual3265(int a, int b) {
    char sa[16], sb[16], ta[16], tb[16];
    sprintf(ta, "%d", a);
    sprintf(tb, "%d", b);
    int wa = (int)strlen(ta), wb = (int)strlen(tb);
    int w = wa > wb ? wa : wb;
    toStrPad(a, sa, w);
    toStrPad(b, sb, w);
    int diff[16], dn = 0;
    for (int i = 0; i < w; i++) if (sa[i] != sb[i]) diff[dn++] = i;
    if (dn == 0) return 1;
    if (dn != 2) return 0;
    int i = diff[0], j = diff[1];
    return sa[i] == sb[j] && sa[j] == sb[i];
}

int countPairs(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++)
        for (int j = i + 1; j < numsSize; j++)
            if (almostEqual3265(nums[i], nums[j])) ans++;
    return ans;
}
