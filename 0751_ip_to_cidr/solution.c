// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static unsigned ipToInt(char* ip) {
    unsigned a, b, c, d;
    sscanf(ip, "%u.%u.%u.%u", &a, &b, &c, &d);
    return (a << 24) | (b << 16) | (c << 8) | d;
}

static void intToIp(unsigned x, char* out) {
    sprintf(out, "%u.%u.%u.%u", (x >> 24) & 255, (x >> 16) & 255, (x >> 8) & 255, x & 255);
}

static int trailingZeros(unsigned x) {
    if (x == 0) return 32;
    int z = 0;
    while ((x & 1u) == 0) { z++; x >>= 1; }
    return z;
}

char** ipToCIDR(char* ip, int n, int* returnSize) {
    unsigned start = ipToInt(ip);
    char** result = (char**)malloc(64 * sizeof(char*));
    int size = 0;
    while (n > 0) {
        int tz = trailingZeros(start);
        int maxBlock = 1 << tz;
        while (maxBlock > n) maxBlock >>= 1;
        int bits = 0;
        int tmp = maxBlock;
        while (tmp > 1) { bits++; tmp >>= 1; }
        char buf[64], ipbuf[32];
        intToIp(start, ipbuf);
        sprintf(buf, "%s/%d", ipbuf, 32 - bits);
        result[size] = (char*)malloc(strlen(buf) + 1);
        strcpy(result[size], buf);
        size++;
        start += (unsigned)maxBlock;
        n -= maxBlock;
    }
    *returnSize = size;
    return result;
}
