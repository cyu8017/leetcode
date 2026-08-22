// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char* left;
    int leftSize;
    int leftCap;
    char* right;
    int rightSize;
    int rightCap;
} TextEditor;

static void ensure(char** buf, int* size, int* cap, int need) {
    if (*cap >= need) return;
    int nc = *cap ? *cap : 16;
    while (nc < need) nc *= 2;
    *buf = (char*)realloc(*buf, (size_t)nc);
    *cap = nc;
}

static char* suffix(TextEditor* obj) {
    int start = obj->leftSize - 10;
    if (start < 0) start = 0;
    int len = obj->leftSize - start;
    char* res = (char*)malloc((size_t)len + 1);
    memcpy(res, obj->left + start, (size_t)len);
    res[len] = '\0';
    return res;
}

TextEditor* textEditorCreate() {
    return (TextEditor*)calloc(1, sizeof(TextEditor));
}

void textEditorAddText(TextEditor* obj, char* text) {
    int n = (int)strlen(text);
    ensure(&obj->left, &obj->leftSize, &obj->leftCap, obj->leftSize + n);
    memcpy(obj->left + obj->leftSize, text, (size_t)n);
    obj->leftSize += n;
}

int textEditorDeleteText(TextEditor* obj, int k) {
    int deleted = 0;
    while (k > 0 && obj->leftSize > 0) {
        obj->leftSize--;
        k--;
        deleted++;
    }
    return deleted;
}

char* textEditorCursorLeft(TextEditor* obj, int k) {
    while (k > 0 && obj->leftSize > 0) {
        ensure(&obj->right, &obj->rightSize, &obj->rightCap, obj->rightSize + 1);
        obj->right[obj->rightSize++] = obj->left[--obj->leftSize];
        k--;
    }
    return suffix(obj);
}

char* textEditorCursorRight(TextEditor* obj, int k) {
    while (k > 0 && obj->rightSize > 0) {
        ensure(&obj->left, &obj->leftSize, &obj->leftCap, obj->leftSize + 1);
        obj->left[obj->leftSize++] = obj->right[--obj->rightSize];
        k--;
    }
    return suffix(obj);
}

void textEditorFree(TextEditor* obj) {
    free(obj->left);
    free(obj->right);
    free(obj);
}
