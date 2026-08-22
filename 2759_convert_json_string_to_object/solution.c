// LeetCode 2759 - Convert JSON String to Object
// https://leetcode.com/problems/convert-json-string-to-object/
// Minimal JSON number/string parse stand-in.

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    int isNumber;
    long long number;
    char* string;
} JsonValue;

JsonValue* jsonParse(char* str) {
    JsonValue* v = (JsonValue*)calloc(1, sizeof(JsonValue));
    while (*str && isspace((unsigned char)*str)) str++;
    if (*str == '"') {
        str++;
        char* end = strchr(str, '"');
        int len = end ? (int)(end - str) : (int)strlen(str);
        v->string = (char*)malloc(len + 1);
        memcpy(v->string, str, len);
        v->string[len] = 0;
        return v;
    }
    v->isNumber = 1;
    v->number = atoll(str);
    return v;
}

void jsonValueFree(JsonValue* v) {
    if (!v) return;
    free(v->string);
    free(v);
}
