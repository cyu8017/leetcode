// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

#include <string.h>
#include <stdbool.h>

typedef struct { char ch; int cnt; } Group;

static int make_groups(const char* text, Group* out) {
    int n = (int)strlen(text), i = 0, g = 0;
    while (i < n) {
        int j = i;
        while (j < n && text[j] == text[i]) j++;
        out[g].ch = text[i];
        out[g].cnt = j - i;
        g++;
        i = j;
    }
    return g;
}

static bool stretchy(const char* word, Group* target, int tlen) {
    Group source[101];
    int slen = make_groups(word, source);
    if (slen != tlen) return false;
    for (int i = 0; i < slen; i++) {
        if (source[i].ch != target[i].ch) return false;
        if (source[i].cnt > target[i].cnt) return false;
        if (source[i].cnt != target[i].cnt && target[i].cnt < 3) return false;
    }
    return true;
}

int expressiveWords(char* s, char** words, int wordsSize) {
    Group target[101];
    int tlen = make_groups(s, target);
    int ans = 0;
    for (int i = 0; i < wordsSize; i++)
        if (stretchy(words[i], target, tlen)) ans++;
    return ans;
}
