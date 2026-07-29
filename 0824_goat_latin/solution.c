// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>

static bool is_vowel(char c) {
    c = (char)tolower((unsigned char)c);
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

char* toGoatLatin(char* sentence) {
    int n = (int)strlen(sentence);
    char* ans = (char*)malloc((size_t)n * 4 + 64);
    ans[0] = '\0';
    int idx = 1;
    char* copy = (char*)malloc((size_t)n + 1);
    strcpy(copy, sentence);
    for (char* word = strtok(copy, " "); word; word = strtok(NULL, " "), idx++) {
        char buf[400];
        if (is_vowel(word[0])) sprintf(buf, "%sma", word);
        else sprintf(buf, "%s%cma", word + 1, word[0]);
        for (int i = 0; i < idx; i++) strcat(buf, "a");
        if (ans[0]) strcat(ans, " ");
        strcat(ans, buf);
    }
    free(copy);
    return ans;
}
