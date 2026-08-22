// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

#include <stdlib.h>
#include <string.h>

struct HtmlParser {
    char** (*getUrls)(char* url, int* returnSize);
};

static void getHost(char* url, char* host, int cap) {
    char* p = url;
    if (strncmp(p, "http://", 7) == 0) p += 7;
    else if (strncmp(p, "https://", 8) == 0) p += 8;
    int i = 0;
    while (p[i] && p[i] != '/' && i < cap - 1) {
        host[i] = p[i];
        i++;
    }
    host[i] = '\0';
}

static int cmpStr(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

char** crawl(char* startUrl, struct HtmlParser* htmlParser, int* returnSize) {
    char host[256];
    getHost(startUrl, host, 256);
    char** seen = (char**)malloc(1000 * sizeof(char*));
    int seenCount = 0;
    char** stack = (char**)malloc(1000 * sizeof(char*));
    int stackSize = 0;
    stack[stackSize++] = startUrl;
    seen[seenCount++] = startUrl;
    while (stackSize > 0) {
        char* url = stack[--stackSize];
        int urlCount = 0;
        char** urls = htmlParser->getUrls(url, &urlCount);
        for (int i = 0; i < urlCount; i++) {
            char urlHost[256];
            getHost(urls[i], urlHost, 256);
            if (strcmp(urlHost, host) != 0) continue;
            int found = 0;
            for (int j = 0; j < seenCount; j++) {
                if (strcmp(seen[j], urls[i]) == 0) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                seen[seenCount++] = urls[i];
                stack[stackSize++] = urls[i];
            }
        }
    }
    qsort(seen, (size_t)seenCount, sizeof(char*), cmpStr);
    *returnSize = seenCount;
    free(stack);
    return seen;
}
