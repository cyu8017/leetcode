// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_URLS 10000
#define MAX_URL_LEN 512

typedef struct {
    char longUrl[MAX_URL_LEN];
    char shortUrl[MAX_URL_LEN];
} UrlPair;

static UrlPair pairs[MAX_URLS];
static int pairCount = 0;
static int counter = 0;
static const char* base = "http://tinyurl.com/";

static char* find_short_url(const char* longUrl) {
    for (int index = 0; index < pairCount; index++) {
        if (strcmp(pairs[index].longUrl, longUrl) == 0) {
            return pairs[index].shortUrl;
        }
    }
    return NULL;
}

char* encode(char* longUrl) {
    char* existing = find_short_url(longUrl);
    if (existing) {
        return existing;
    }

    if (pairCount >= MAX_URLS) {
        return NULL;
    }

    snprintf(pairs[pairCount].shortUrl, MAX_URL_LEN, "%s%d", base, counter++);
    strncpy(pairs[pairCount].longUrl, longUrl, MAX_URL_LEN - 1);
    pairs[pairCount].longUrl[MAX_URL_LEN - 1] = '\0';
    return pairs[pairCount++].shortUrl;
}

char* decode(char* shortUrl) {
    for (int index = 0; index < pairCount; index++) {
        if (strcmp(pairs[index].shortUrl, shortUrl) == 0) {
            return pairs[index].longUrl;
        }
    }
    return NULL;
}
