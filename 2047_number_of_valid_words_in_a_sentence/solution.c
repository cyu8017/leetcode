// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

#include <stdbool.h>
#include <string.h>

static bool valid2047(const char* w, int len) {
    if (len == 0) return false;
    int hyphen = 0;
    for (int i = 0; i < len; i++) {
        char c = w[i];
        if (c >= '0' && c <= '9') return false;
        if (c == '-') {
            hyphen++;
            if (hyphen > 1 || i == 0 || i == len - 1) return false;
            if (w[i - 1] < 'a' || w[i - 1] > 'z' || w[i + 1] < 'a' || w[i + 1] > 'z') return false;
        } else if (c == '!' || c == '.' || c == ',') {
            if (i != len - 1) return false;
        } else if (c < 'a' || c > 'z') return false;
    }
    return true;
}

int countValidWords(char* sentence) {
    int ans = 0, n = (int)strlen(sentence);
    int i = 0;
    while (i < n) {
        while (i < n && sentence[i] == ' ') i++;
        if (i >= n) break;
        int start = i;
        while (i < n && sentence[i] != ' ') i++;
        if (valid2047(sentence + start, i - start)) ans++;
    }
    return ans;
}
