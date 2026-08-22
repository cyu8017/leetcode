// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

#include <stdlib.h>
#include <string.h>

typedef void (*EventCallback)(void* args);

typedef struct {
    char* name;
    EventCallback* cbs;
    int size;
    int cap;
} EventEntry;

typedef struct {
    EventEntry* entries;
    int size;
    int cap;
} EventEmitter;

EventEmitter* eventEmitterCreate(void) {
    return (EventEmitter*)calloc(1, sizeof(EventEmitter));
}

static EventEntry* findEntry(EventEmitter* e, const char* name, int create) {
    for (int i = 0; i < e->size; i++)
        if (strcmp(e->entries[i].name, name) == 0) return &e->entries[i];
    if (!create) return NULL;
    if (e->size == e->cap) {
        e->cap = e->cap ? e->cap * 2 : 4;
        e->entries = (EventEntry*)realloc(e->entries, (size_t)e->cap * sizeof(EventEntry));
    }
    EventEntry* en = &e->entries[e->size++];
    memset(en, 0, sizeof(*en));
    en->name = (char*)malloc(strlen(name) + 1);
    strcpy(en->name, name);
    return en;
}

int eventEmitterSubscribe(EventEmitter* e, char* eventName, EventCallback cb) {
    EventEntry* en = findEntry(e, eventName, 1);
    if (en->size == en->cap) {
        en->cap = en->cap ? en->cap * 2 : 4;
        en->cbs = (EventCallback*)realloc(en->cbs, (size_t)en->cap * sizeof(EventCallback));
    }
    en->cbs[en->size++] = cb;
    return en->size - 1;
}

void eventEmitterUnsubscribe(EventEmitter* e, char* eventName, int idx) {
    EventEntry* en = findEntry(e, eventName, 0);
    if (!en || idx < 0 || idx >= en->size) return;
    for (int i = idx; i + 1 < en->size; i++) en->cbs[i] = en->cbs[i + 1];
    en->size--;
}

int eventEmitterEmit(EventEmitter* e, char* eventName, void* args) {
    EventEntry* en = findEntry(e, eventName, 0);
    if (!en) return 0;
    for (int i = 0; i < en->size; i++)
        if (en->cbs[i]) en->cbs[i](args);
    return en->size;
}

void eventEmitterFree(EventEmitter* e) {
    if (!e) return;
    for (int i = 0; i < e->size; i++) {
        free(e->entries[i].name);
        free(e->entries[i].cbs);
    }
    free(e->entries);
    free(e);
}
