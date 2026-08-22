// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

typedef struct {
    char** rows; /* each row is comma-joined string starting with id */
    int size;
    int cap;
    int nextID;
} Table;

typedef struct {
    char** names;
    Table* tables;
    int n;
} SQL;

SQL* sQLCreate(char** names, int namesSize, int* columns, int columnsSize) {
    (void)columns; (void)columnsSize;
    SQL* obj = (SQL*)malloc(sizeof(SQL));
    obj->n = namesSize;
    obj->names = names;
    obj->tables = (Table*)calloc((size_t)namesSize, sizeof(Table));
    for (int i = 0; i < namesSize; i++) obj->tables[i].nextID = 1;
    return obj;
}

static int findTable(SQL* obj, char* name) {
    for (int i = 0; i < obj->n; i++) if (strcmp(obj->names[i], name) == 0) return i;
    return -1;
}

bool sQLIns(SQL* obj, char* name, char** row, int rowSize) {
    int ti = findTable(obj, name);
    if (ti < 0) return false;
    Table* t = &obj->tables[ti];
    if (t->size >= t->cap) {
        t->cap = t->cap ? t->cap * 2 : 4;
        t->rows = (char**)realloc(t->rows, (size_t)t->cap * sizeof(char*));
    }
    int len = 32;
    for (int i = 0; i < rowSize; i++) len += (int)strlen(row[i]) + 1;
    char* full = (char*)malloc((size_t)len);
    sprintf(full, "%d", t->nextID++);
    for (int i = 0; i < rowSize; i++) { strcat(full, ","); strcat(full, row[i]); }
    t->rows[t->size++] = full;
    return true;
}

void sQLRmv(SQL* obj, char* name, int rowId) {
    int ti = findTable(obj, name);
    if (ti < 0) return;
    Table* t = &obj->tables[ti];
    for (int i = 0; i < t->size; i++) {
        int id = atoi(t->rows[i]);
        if (id == rowId) {
            free(t->rows[i]);
            for (int j = i; j + 1 < t->size; j++) t->rows[j] = t->rows[j + 1];
            t->size--;
            return;
        }
    }
}

char* sQLSel(SQL* obj, char* name, int rowId, int columnId) {
    static char nullstr[] = "<null>";
    int ti = findTable(obj, name);
    if (ti < 0) return nullstr;
    Table* t = &obj->tables[ti];
    for (int i = 0; i < t->size; i++) {
        if (atoi(t->rows[i]) != rowId) continue;
        /* split by comma */
        char* copy = (char*)malloc(strlen(t->rows[i]) + 1);
        strcpy(copy, t->rows[i]);
        char* parts[64]; int pc = 0;
        char* tok = strtok(copy, ",");
        while (tok) { parts[pc++] = tok; tok = strtok(NULL, ","); }
        if (columnId < 1 || columnId >= pc) { free(copy); return nullstr; }
        char* res = (char*)malloc(strlen(parts[columnId]) + 1);
        strcpy(res, parts[columnId]);
        free(copy);
        return res;
    }
    return nullstr;
}

char** sQLExp(SQL* obj, char* name, int* retSize) {
    int ti = findTable(obj, name);
    if (ti < 0) { *retSize = 0; return NULL; }
    Table* t = &obj->tables[ti];
    char** ans = (char**)malloc((size_t)t->size * sizeof(char*));
    for (int i = 0; i < t->size; i++) {
        ans[i] = (char*)malloc(strlen(t->rows[i]) + 1);
        strcpy(ans[i], t->rows[i]);
    }
    *retSize = t->size;
    return ans;
}

void sQLFree(SQL* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->n; i++) {
        for (int j = 0; j < obj->tables[i].size; j++) free(obj->tables[i].rows[j]);
        free(obj->tables[i].rows);
    }
    free(obj->tables);
    free(obj);
}
