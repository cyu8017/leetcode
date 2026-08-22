// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>

#define MAX_TERMS 256
#define MAX_VARS 8
#define MAX_TOKENS 512

typedef struct {
    char vars[MAX_VARS][16];
    int varCount;
    int coef;
} Term;

typedef struct {
    Term terms[MAX_TERMS];
    int size;
} Poly;

static char* g_tokens[MAX_TOKENS];
static int g_tokenCount;
static int g_pos;
static char g_evalNames[100][16];
static int g_evalVals[100];
static int g_evalCount;

static int cmpStr(const void* a, const void* b) {
    return strcmp((const char*)a, (const char*)b);
}

static void termSortVars(Term* t) {
    qsort(t->vars, (size_t)t->varCount, 16, cmpStr);
}

static bool termKeyEq(const Term* a, const Term* b) {
    if (a->varCount != b->varCount) return false;
    for (int i = 0; i < a->varCount; i++) {
        if (strcmp(a->vars[i], b->vars[i]) != 0) return false;
    }
    return true;
}

static void polyAddTerm(Poly* p, Term t) {
    if (t.coef == 0) return;
    for (int i = 0; i < p->size; i++) {
        if (termKeyEq(&p->terms[i], &t)) {
            p->terms[i].coef += t.coef;
            if (p->terms[i].coef == 0) {
                p->terms[i] = p->terms[p->size - 1];
                p->size--;
            }
            return;
        }
    }
    p->terms[p->size++] = t;
}

static Poly polyAdd(Poly a, Poly b) {
    Poly r = a;
    for (int i = 0; i < b.size; i++) polyAddTerm(&r, b.terms[i]);
    return r;
}

static Poly polyNeg(Poly a) {
    for (int i = 0; i < a.size; i++) a.terms[i].coef = -a.terms[i].coef;
    return a;
}

static Poly polyMul(Poly a, Poly b) {
    Poly r = {0};
    for (int i = 0; i < a.size; i++) {
        for (int j = 0; j < b.size; j++) {
            Term t = {0};
            t.coef = a.terms[i].coef * b.terms[j].coef;
            t.varCount = 0;
            for (int x = 0; x < a.terms[i].varCount; x++) {
                strcpy(t.vars[t.varCount++], a.terms[i].vars[x]);
            }
            for (int x = 0; x < b.terms[j].varCount; x++) {
                strcpy(t.vars[t.varCount++], b.terms[j].vars[x]);
            }
            termSortVars(&t);
            polyAddTerm(&r, t);
        }
    }
    return r;
}

static int evalLookup(const char* name, bool* found) {
    for (int i = 0; i < g_evalCount; i++) {
        if (strcmp(g_evalNames[i], name) == 0) {
            *found = true;
            return g_evalVals[i];
        }
    }
    *found = false;
    return 0;
}

static Poly atom(const char* token) {
    Poly p = {0};
    Term t = {0};
    if (isalpha((unsigned char)token[0])) {
        bool found = false;
        int v = evalLookup(token, &found);
        if (found) {
            t.coef = v;
        } else {
            t.coef = 1;
            strcpy(t.vars[0], token);
            t.varCount = 1;
        }
    } else {
        t.coef = atoi(token);
    }
    polyAddTerm(&p, t);
    return p;
}

static Poly parseExpr(void);
static Poly parseTerm(void);
static Poly parseFactor(void);

static Poly parseFactor(void) {
    char* token = g_tokens[g_pos];
    if (strcmp(token, "(") == 0) {
        g_pos++;
        Poly p = parseExpr();
        g_pos++; /* ) */
        return p;
    }
    g_pos++;
    return atom(token);
}

static Poly parseTerm(void) {
    Poly p = parseFactor();
    while (g_pos < g_tokenCount && strcmp(g_tokens[g_pos], "*") == 0) {
        g_pos++;
        p = polyMul(p, parseFactor());
    }
    return p;
}

static Poly parseExpr(void) {
    Poly p = parseTerm();
    while (g_pos < g_tokenCount && (strcmp(g_tokens[g_pos], "+") == 0 || strcmp(g_tokens[g_pos], "-") == 0)) {
        char* op = g_tokens[g_pos++];
        Poly right = parseTerm();
        if (strcmp(op, "+") == 0) p = polyAdd(p, right);
        else p = polyAdd(p, polyNeg(right));
    }
    return p;
}

static int cmpTermKey(const void* a, const void* b) {
    const Term* x = (const Term*)a;
    const Term* y = (const Term*)b;
    if (x->varCount != y->varCount) return y->varCount - x->varCount;
    for (int i = 0; i < x->varCount; i++) {
        int c = strcmp(x->vars[i], y->vars[i]);
        if (c) return c;
    }
    return 0;
}

char** basicCalculatorIV(char* expression, char** evalvars, int evalvarsSize, int* evalints, int evalintsSize, int* returnSize) {
    (void)evalintsSize;
    g_evalCount = evalvarsSize;
    for (int i = 0; i < evalvarsSize; i++) {
        strncpy(g_evalNames[i], evalvars[i], 15);
        g_evalNames[i][15] = '\0';
        g_evalVals[i] = evalints[i];
    }

    char* buf = (char*)malloc(strlen(expression) * 3 + 1);
    int bi = 0;
    for (char* p = expression; *p; p++) {
        if (*p == '(' || *p == ')' || *p == '+' || *p == '-' || *p == '*') {
            buf[bi++] = ' ';
            buf[bi++] = *p;
            buf[bi++] = ' ';
        } else {
            buf[bi++] = *p;
        }
    }
    buf[bi] = '\0';
    g_tokenCount = 0;
    for (char* tok = strtok(buf, " \t"); tok; tok = strtok(NULL, " \t")) {
        g_tokens[g_tokenCount++] = tok;
    }
    g_pos = 0;
    Poly poly = parseExpr();
    qsort(poly.terms, (size_t)poly.size, sizeof(Term), cmpTermKey);

    char** answer = (char**)malloc((size_t)poly.size * sizeof(char*));
    int asize = 0;
    for (int i = 0; i < poly.size; i++) {
        if (poly.terms[i].coef == 0) continue;
        char* line = (char*)malloc(256);
        if (poly.terms[i].varCount == 0) {
            sprintf(line, "%d", poly.terms[i].coef);
        } else {
            int pos = sprintf(line, "%d", poly.terms[i].coef);
            for (int v = 0; v < poly.terms[i].varCount; v++) {
                pos += sprintf(line + pos, "*%s", poly.terms[i].vars[v]);
            }
        }
        answer[asize++] = line;
    }
    free(buf);
    *returnSize = asize;
    return answer;
}
