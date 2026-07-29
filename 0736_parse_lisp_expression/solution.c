// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

typedef struct {
    char* key;
    int value;
} Binding;

typedef struct {
    Binding* items;
    int size;
    int capacity;
} Scope;

static char** tokenize(char* expression, int* count) {
    char* buf = (char*)malloc(strlen(expression) * 3 + 1);
    int bi = 0;
    for (char* p = expression; *p; p++) {
        if (*p == '(' || *p == ')') {
            buf[bi++] = ' ';
            buf[bi++] = *p;
            buf[bi++] = ' ';
        } else {
            buf[bi++] = *p;
        }
    }
    buf[bi] = '\0';
    char** tokens = (char**)malloc(5000 * sizeof(char*));
    int n = 0;
    char* tok = strtok(buf, " \t\n");
    while (tok) {
        tokens[n] = (char*)malloc(strlen(tok) + 1);
        strcpy(tokens[n], tok);
        n++;
        tok = strtok(NULL, " \t\n");
    }
    free(buf);
    *count = n;
    return tokens;
}

static int lookup(Scope* env, int envSize, const char* name) {
    for (int s = envSize - 1; s >= 0; s--) {
        for (int i = 0; i < env[s].size; i++) {
            if (strcmp(env[s].items[i].key, name) == 0) {
                return env[s].items[i].value;
            }
        }
    }
    return 0;
}

static void scopeSet(Scope* scope, const char* key, int value) {
    for (int i = 0; i < scope->size; i++) {
        if (strcmp(scope->items[i].key, key) == 0) {
            scope->items[i].value = value;
            return;
        }
    }
    if (scope->size == scope->capacity) {
        scope->capacity = scope->capacity ? scope->capacity * 2 : 8;
        scope->items = (Binding*)realloc(scope->items, (size_t)scope->capacity * sizeof(Binding));
    }
    scope->items[scope->size].key = (char*)malloc(strlen(key) + 1);
    strcpy(scope->items[scope->size].key, key);
    scope->items[scope->size].value = value;
    scope->size++;
}

static int parse(char** tokens, int* pos, int tokenCount, Scope* env, int* envSize);

static int parse(char** tokens, int* pos, int tokenCount, Scope* env, int* envSize) {
    char* token = tokens[*pos];
    if (strcmp(token, "(") != 0) {
        (*pos)++;
        if (isdigit((unsigned char)token[0]) || (token[0] == '-' && isdigit((unsigned char)token[1]))) {
            return atoi(token);
        }
        return lookup(env, *envSize, token);
    }
    (*pos)++;
    char* op = tokens[*pos];
    (*pos)++;
    if (strcmp(op, "let") == 0) {
        env[(*envSize)++] = (Scope){0};
        while (strcmp(tokens[*pos], ")") != 0) {
            if (strcmp(tokens[*pos], "(") == 0 || strcmp(tokens[*pos + 1], ")") == 0) {
                int value = parse(tokens, pos, tokenCount, env, envSize);
                (*pos)++;
                Scope top = env[--(*envSize)];
                for (int i = 0; i < top.size; i++) free(top.items[i].key);
                free(top.items);
                return value;
            }
            char* var = tokens[*pos];
            (*pos)++;
            int value = parse(tokens, pos, tokenCount, env, envSize);
            scopeSet(&env[*envSize - 1], var, value);
        }
    }
    if (strcmp(op, "add") == 0) {
        int left = parse(tokens, pos, tokenCount, env, envSize);
        int right = parse(tokens, pos, tokenCount, env, envSize);
        (*pos)++;
        return left + right;
    }
    if (strcmp(op, "mult") == 0) {
        int left = parse(tokens, pos, tokenCount, env, envSize);
        int right = parse(tokens, pos, tokenCount, env, envSize);
        (*pos)++;
        return left * right;
    }
    return 0;
}

int evaluate(char* expression) {
    int tokenCount = 0;
    char** tokens = tokenize(expression, &tokenCount);
    Scope env[64];
    int envSize = 0;
    int pos = 0;
    int result = parse(tokens, &pos, tokenCount, env, &envSize);
    for (int i = 0; i < tokenCount; i++) free(tokens[i]);
    free(tokens);
    return result;
}
