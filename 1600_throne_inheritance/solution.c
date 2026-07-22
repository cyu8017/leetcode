// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_PEOPLE 100005
#define MAX_NAME 16
#define HASH_SIZE 200003

typedef struct {
    char name[MAX_NAME];
    int* children;
    int childCount;
    int childCap;
    bool dead;
} Person;

typedef struct {
    Person* people;
    int count;
    int king;
    int* hashTable;
} ThroneInheritance;

static unsigned hashStr(const char* s) {
    unsigned h = 2166136261u;
    while (*s) {
        h ^= (unsigned char)(*s++);
        h *= 16777619u;
    }
    return h % HASH_SIZE;
}

static int findPerson(ThroneInheritance* obj, const char* name) {
    unsigned h = hashStr(name);
    for (int i = 0; i < HASH_SIZE; i++) {
        int idx = obj->hashTable[(h + i) % HASH_SIZE];
        if (idx < 0) return -1;
        if (strcmp(obj->people[idx].name, name) == 0) return idx;
    }
    return -1;
}

static int addPerson(ThroneInheritance* obj, const char* name) {
    int id = obj->count++;
    Person* p = &obj->people[id];
    memset(p, 0, sizeof(*p));
    strncpy(p->name, name, MAX_NAME - 1);
    unsigned h = hashStr(name);
    for (int i = 0; i < HASH_SIZE; i++) {
        int slot = (h + i) % HASH_SIZE;
        if (obj->hashTable[slot] < 0) {
            obj->hashTable[slot] = id;
            return id;
        }
    }
    return id;
}

static int getOrAdd(ThroneInheritance* obj, const char* name) {
    int id = findPerson(obj, name);
    if (id >= 0) return id;
    return addPerson(obj, name);
}

ThroneInheritance* throneInheritanceCreate(char* kingName) {
    ThroneInheritance* obj = (ThroneInheritance*)calloc(1, sizeof(ThroneInheritance));
    obj->people = (Person*)calloc(MAX_PEOPLE, sizeof(Person));
    obj->hashTable = (int*)malloc(HASH_SIZE * sizeof(int));
    for (int i = 0; i < HASH_SIZE; i++) obj->hashTable[i] = -1;
    obj->king = addPerson(obj, kingName);
    return obj;
}

void throneInheritanceBirth(ThroneInheritance* obj, char* parentName, char* childName) {
    int parent = getOrAdd(obj, parentName);
    int child = getOrAdd(obj, childName);
    Person* p = &obj->people[parent];
    if (p->childCount == p->childCap) {
        p->childCap = p->childCap ? p->childCap * 2 : 4;
        p->children = (int*)realloc(p->children, (size_t)p->childCap * sizeof(int));
    }
    p->children[p->childCount++] = child;
}

void throneInheritanceDeath(ThroneInheritance* obj, char* name) {
    int id = findPerson(obj, name);
    if (id >= 0) obj->people[id].dead = true;
}

static void dfsOrder(ThroneInheritance* obj, int id, char** out, int* size) {
    Person* p = &obj->people[id];
    if (!p->dead) {
        out[*size] = (char*)malloc(MAX_NAME);
        strcpy(out[*size], p->name);
        (*size)++;
    }
    for (int i = 0; i < p->childCount; i++) dfsOrder(obj, p->children[i], out, size);
}

char** throneInheritanceGetInheritanceOrder(ThroneInheritance* obj, int* retSize) {
    char** out = (char**)malloc((size_t)obj->count * sizeof(char*));
    *retSize = 0;
    dfsOrder(obj, obj->king, out, retSize);
    return out;
}

void throneInheritanceFree(ThroneInheritance* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->count; i++) free(obj->people[i].children);
    free(obj->people);
    free(obj->hashTable);
    free(obj);
}
