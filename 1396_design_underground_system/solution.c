// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

#include <stdlib.h>
#include <string.h>

typedef struct { int id; char* station; int t; } CheckIn;
typedef struct { char* start; char* end; double total; int count; } Stat;

typedef struct {
    CheckIn* ins;
    int inSize, inCap;
    Stat* stats;
    int stSize, stCap;
} UndergroundSystem;

UndergroundSystem* undergroundSystemCreate() {
    UndergroundSystem* obj = (UndergroundSystem*)calloc(1, sizeof(UndergroundSystem));
    obj->inCap = 16; obj->ins = (CheckIn*)malloc(obj->inCap * sizeof(CheckIn));
    obj->stCap = 16; obj->stats = (Stat*)malloc(obj->stCap * sizeof(Stat));
    return obj;
}

void undergroundSystemCheckIn(UndergroundSystem* obj, int id, char* stationName, int t) {
    if (obj->inSize == obj->inCap) {
        obj->inCap *= 2;
        obj->ins = (CheckIn*)realloc(obj->ins, obj->inCap * sizeof(CheckIn));
    }
    CheckIn* c = &obj->ins[obj->inSize++];
    c->id = id;
    c->station = (char*)malloc(strlen(stationName) + 1);
    strcpy(c->station, stationName);
    c->t = t;
}

void undergroundSystemCheckOut(UndergroundSystem* obj, int id, char* stationName, int t) {
    int idx = -1;
    for (int i = 0; i < obj->inSize; i++) if (obj->ins[i].id == id) { idx = i; break; }
    char* start = obj->ins[idx].station;
    int begin = obj->ins[idx].t;
    obj->ins[idx] = obj->ins[--obj->inSize];
    int found = -1;
    for (int i = 0; i < obj->stSize; i++)
        if (strcmp(obj->stats[i].start, start) == 0 && strcmp(obj->stats[i].end, stationName) == 0) {
            found = i; break;
        }
    if (found < 0) {
        if (obj->stSize == obj->stCap) {
            obj->stCap *= 2;
            obj->stats = (Stat*)realloc(obj->stats, obj->stCap * sizeof(Stat));
        }
        found = obj->stSize++;
        obj->stats[found].start = (char*)malloc(strlen(start) + 1);
        strcpy(obj->stats[found].start, start);
        obj->stats[found].end = (char*)malloc(strlen(stationName) + 1);
        strcpy(obj->stats[found].end, stationName);
        obj->stats[found].total = 0;
        obj->stats[found].count = 0;
    }
    obj->stats[found].total += t - begin;
    obj->stats[found].count++;
    free(start);
}

double undergroundSystemGetAverageTime(UndergroundSystem* obj, char* startStation, char* endStation) {
    for (int i = 0; i < obj->stSize; i++)
        if (strcmp(obj->stats[i].start, startStation) == 0 && strcmp(obj->stats[i].end, endStation) == 0)
            return obj->stats[i].total / obj->stats[i].count;
    return 0;
}

void undergroundSystemFree(UndergroundSystem* obj) {
    for (int i = 0; i < obj->inSize; i++) free(obj->ins[i].station);
    for (int i = 0; i < obj->stSize; i++) { free(obj->stats[i].start); free(obj->stats[i].end); }
    free(obj->ins); free(obj->stats); free(obj);
}
