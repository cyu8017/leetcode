// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

#include <stdlib.h>
#include <string.h>

#define ENC_HASH 20011

typedef struct EncNode {
    char* key;
    int cnt;
    struct EncNode* next;
} EncNode;

typedef struct {
    char* enc[128];
    EncNode* cnt[ENC_HASH];
} Encrypter;

static unsigned hash_str(const char* s) {
    unsigned h = 2166136261u;
    while (*s) { h ^= (unsigned char)(*s++); h *= 16777619u; }
    return h % ENC_HASH;
}

static void cnt_add(Encrypter* obj, const char* s) {
    if (!s || !s[0]) return;
    unsigned h = hash_str(s);
    for (EncNode* p = obj->cnt[h]; p; p = p->next) {
        if (strcmp(p->key, s) == 0) { p->cnt++; return; }
    }
    EncNode* n = (EncNode*)malloc(sizeof(EncNode));
    n->key = strdup(s);
    n->cnt = 1;
    n->next = obj->cnt[h];
    obj->cnt[h] = n;
}

static int cnt_get(Encrypter* obj, const char* s) {
    unsigned h = hash_str(s);
    for (EncNode* p = obj->cnt[h]; p; p = p->next) {
        if (strcmp(p->key, s) == 0) return p->cnt;
    }
    return 0;
}

char* encrypterEncrypt(Encrypter* obj, char* word1);

Encrypter* encrypterCreate(char* keys, int keysSize, char** values, int valuesSize, char** dictionary, int dictionarySize) {
    (void)valuesSize;
    Encrypter* obj = (Encrypter*)calloc(1, sizeof(Encrypter));
    for (int i = 0; i < keysSize; i++) {
        obj->enc[(unsigned char)keys[i]] = values[i];
    }
    for (int i = 0; i < dictionarySize; i++) {
        char* e = encrypterEncrypt(obj, dictionary[i]);
        cnt_add(obj, e);
        free(e);
    }
    return obj;
}

char* encrypterEncrypt(Encrypter* obj, char* word1) {
    int n = (int)strlen(word1);
    char* b = (char*)malloc((size_t)n * 2 + 1);
    int pos = 0;
    for (int i = 0; i < n; i++) {
        char* v = obj->enc[(unsigned char)word1[i]];
        if (!v) { b[0] = '\0'; return b; }
        b[pos++] = v[0];
        b[pos++] = v[1];
    }
    b[pos] = '\0';
    return b;
}

int encrypterDecrypt(Encrypter* obj, char* word2) {
    return cnt_get(obj, word2);
}

void encrypterFree(Encrypter* obj) {
    for (int i = 0; i < ENC_HASH; i++) {
        EncNode* p = obj->cnt[i];
        while (p) {
            EncNode* n = p->next;
            free(p->key);
            free(p);
            p = n;
        }
    }
    free(obj);
}
