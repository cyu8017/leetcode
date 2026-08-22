// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool starts_with(const char* first, const char* second) {
    size_t second_len = strlen(second);
    return strncmp(first, second, second_len) == 0;
}

char* alienOrder(char** words, int wordsSize) {
    bool present[256] = {false};
    int indegree[256] = {0};
    bool graph[256][256] = {{false}};

    for (int i = 0; i < wordsSize; ++i) {
        for (int j = 0; words[i][j] != '\0'; ++j) {
            present[(unsigned char)words[i][j]] = true;
        }
    }

    for (int i = 0; i < wordsSize - 1; ++i) {
        const char* first = words[i];
        const char* second = words[i + 1];
        if (strlen(first) > strlen(second) && starts_with(first, second)) {
            char* empty = (char*)malloc(1);
            empty[0] = '\0';
            return empty;
        }
        size_t limit = strlen(first);
        size_t second_len = strlen(second);
        if (second_len < limit) {
            limit = second_len;
        }
        for (size_t j = 0; j < limit; ++j) {
            unsigned char left = (unsigned char)first[j];
            unsigned char right = (unsigned char)second[j];
            if (left != right) {
                if (!graph[left][right]) {
                    graph[left][right] = true;
                    indegree[right]++;
                }
                break;
            }
        }
    }

    int queue[256];
    int head = 0;
    int tail = 0;
    for (int ch = 0; ch < 256; ++ch) {
        if (present[ch] && indegree[ch] == 0) {
            queue[tail++] = ch;
        }
    }

    char order[256];
    int order_size = 0;
    while (head < tail) {
        int ch = queue[head++];
        order[order_size++] = (char)ch;
        for (int next = 0; next < 256; ++next) {
            if (graph[ch][next]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    queue[tail++] = next;
                }
            }
        }
    }

    int char_count = 0;
    for (int ch = 0; ch < 256; ++ch) {
        if (present[ch]) {
            char_count++;
        }
    }

    char* result = (char*)malloc((size_t)order_size + 1);
    if (order_size != char_count) {
        result[0] = '\0';
        return result;
    }
    memcpy(result, order, (size_t)order_size);
    result[order_size] = '\0';
    return result;
}
