// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int uniqueMorseRepresentations(char** words, int wordsSize) {
    static const char* codes[] = {
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    };
    char** seen = (char**)malloc((size_t)wordsSize * sizeof(char*));
    int count = 0;
    for (int i = 0; i < wordsSize; i++) {
        char buf[100] = {0};
        int pos = 0;
        for (char* p = words[i]; *p; p++) {
            const char* code = codes[*p - 'a'];
            int len = (int)strlen(code);
            memcpy(buf + pos, code, (size_t)len);
            pos += len;
        }
        buf[pos] = '\0';
        bool found = false;
        for (int j = 0; j < count; j++) {
            if (strcmp(seen[j], buf) == 0) {
                found = true;
                break;
            }
        }
        if (!found) {
            seen[count] = (char*)malloc((size_t)pos + 1);
            strcpy(seen[count], buf);
            count++;
        }
    }
    for (int i = 0; i < count; i++) free(seen[i]);
    free(seen);
    return count;
}
