// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

#include <pthread.h>
#include <stdlib.h>
#include <string.h>

struct HtmlParser;

struct HtmlParser {
    char** (*getUrls)(struct HtmlParser*, char*, int*);
};

typedef struct {
    char* url;
    struct HtmlParser* parser;
    char*** batchUrls;
    int* batchSizes;
    int index;
} FetchTask;

static char* extract_host(const char* url) {
    const char* start = strstr(url, "://");
    start = start ? start + 3 : url;
    const char* end = strchr(start, '/');
    int len = end ? (int)(end - start) : (int)strlen(start);
    char* host = (char*)malloc((size_t)len + 1);
    memcpy(host, start, (size_t)len);
    host[len] = '\0';
    return host;
}

static int same_host(const char* host, const char* url) {
    const char* start = strstr(url, "://");
    start = start ? start + 3 : url;
    const char* end = strchr(start, '/');
    int len = end ? (int)(end - start) : (int)strlen(start);
    return (int)strlen(host) == len && strncmp(host, start, (size_t)len) == 0;
}

static void* fetch_worker(void* arg) {
    FetchTask* task = (FetchTask*)arg;
    task->batchUrls[task->index] = task->parser->getUrls(task->parser, task->url, &task->batchSizes[task->index]);
    return NULL;
}

static int cmp_str(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

char** crawl(char* startUrl, struct HtmlParser* parser, int* returnSize) {
    char* host = extract_host(startUrl);
    int cap = 16, seenCount = 0;
    char** seen = (char**)malloc((size_t)cap * sizeof(char*));
    seen[seenCount++] = startUrl;
    char** frontier = (char**)malloc(sizeof(char*));
    frontier[0] = startUrl;
    int frontierSize = 1;
    while (frontierSize > 0) {
        char*** batchUrls = (char***)malloc((size_t)frontierSize * sizeof(char**));
        int* batchSizes = (int*)malloc((size_t)frontierSize * sizeof(int));
        FetchTask* tasks = (FetchTask*)malloc((size_t)frontierSize * sizeof(FetchTask));
        pthread_t* threads = (pthread_t*)malloc((size_t)frontierSize * sizeof(pthread_t));
        for (int i = 0; i < frontierSize; i++) {
            tasks[i] = (FetchTask){frontier[i], parser, batchUrls, batchSizes, i};
            pthread_create(&threads[i], NULL, fetch_worker, &tasks[i]);
        }
        for (int i = 0; i < frontierSize; i++) pthread_join(threads[i], NULL);
        int nextCap = 16, nextSize = 0;
        char** nextFrontier = (char**)malloc((size_t)nextCap * sizeof(char*));
        for (int i = 0; i < frontierSize; i++) {
            for (int j = 0; j < batchSizes[i]; j++) {
                char* url = batchUrls[i][j];
                if (!same_host(host, url)) continue;
                int found = 0;
                for (int k = 0; k < seenCount; k++) {
                    if (strcmp(seen[k], url) == 0) {
                        found = 1;
                        break;
                    }
                }
                if (found) continue;
                if (seenCount >= cap) {
                    cap *= 2;
                    seen = (char**)realloc(seen, (size_t)cap * sizeof(char*));
                }
                seen[seenCount++] = url;
                if (nextSize >= nextCap) {
                    nextCap *= 2;
                    nextFrontier = (char**)realloc(nextFrontier, (size_t)nextCap * sizeof(char*));
                }
                nextFrontier[nextSize++] = url;
            }
        }
        free(frontier);
        free(batchUrls);
        free(batchSizes);
        free(tasks);
        free(threads);
        frontier = nextFrontier;
        frontierSize = nextSize;
    }
    free(frontier);
    free(host);
    qsort(seen, (size_t)seenCount, sizeof(char*), cmp_str);
    *returnSize = seenCount;
    return seen;
}
