// LeetCode 0332 - Reconstruct Itinerary
// https://leetcode.com/problems/reconstruct-itinerary/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char from[4];
    char to[4];
} Ticket;

typedef struct {
    char code[4];
    char** destinations;
    int destCount;
    int destCapacity;
} AirportNode;

typedef struct {
    char** items;
    int size;
    int capacity;
} RouteList;

static int ticketCompare(const void* left, const void* right) {
    const Ticket* a = (const Ticket*)left;
    const Ticket* b = (const Ticket*)right;
    int fromCompare = strcmp(a->from, b->from);
    if (fromCompare != 0) {
        return fromCompare;
    }
    return strcmp(a->to, b->to);
}

static AirportNode* getAirport(AirportNode* graph, int* graphSize, const char* code) {
    for (int index = 0; index < *graphSize; index++) {
        if (strcmp(graph[index].code, code) == 0) {
            return &graph[index];
        }
    }
    AirportNode* node = &graph[(*graphSize)++];
    strncpy(node->code, code, 3);
    node->code[3] = '\0';
    node->destinations = NULL;
    node->destCount = 0;
    node->destCapacity = 0;
    return node;
}

static void addDestination(AirportNode* node, const char* destination) {
    if (node->destCount == node->destCapacity) {
        node->destCapacity = node->destCapacity == 0 ? 4 : node->destCapacity * 2;
        node->destinations = (char**)realloc(
            node->destinations,
            (size_t)node->destCapacity * sizeof(char*)
        );
    }
    node->destinations[node->destCount] = strdup(destination);
    node->destCount += 1;
}

static void routeAdd(RouteList* route, const char* airport) {
    if (route->size == route->capacity) {
        route->capacity = route->capacity == 0 ? 8 : route->capacity * 2;
        route->items = (char**)realloc(route->items, (size_t)route->capacity * sizeof(char*));
    }
    route->items[route->size++] = strdup(airport);
}

static void visit(AirportNode* graph, int graphSize, const char* airport, RouteList* route) {
    AirportNode* node = NULL;
    for (int index = 0; index < graphSize; index++) {
        if (strcmp(graph[index].code, airport) == 0) {
            node = &graph[index];
            break;
        }
    }
    if (node != NULL) {
        while (node->destCount > 0) {
            char* next = node->destinations[node->destCount - 1];
            node->destCount -= 1;
            visit(graph, graphSize, next, route);
            free(next);
        }
    }
    routeAdd(route, airport);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findItinerary(char*** tickets, int ticketsSize, int* ticketsColSize, int* returnSize) {
    Ticket* sortedTickets = (Ticket*)malloc((size_t)ticketsSize * sizeof(Ticket));
    for (int index = 0; index < ticketsSize; index++) {
        strncpy(sortedTickets[index].from, tickets[index][0], 3);
        sortedTickets[index].from[3] = '\0';
        strncpy(sortedTickets[index].to, tickets[index][1], 3);
        sortedTickets[index].to[3] = '\0';
    }
    qsort(sortedTickets, (size_t)ticketsSize, sizeof(Ticket), ticketCompare);

    AirportNode graph[128];
    int graphSize = 0;
    for (int index = ticketsSize - 1; index >= 0; index--) {
        AirportNode* node = getAirport(graph, &graphSize, sortedTickets[index].from);
        addDestination(node, sortedTickets[index].to);
    }
    free(sortedTickets);

    RouteList route = { NULL, 0, 0 };
    visit(graph, graphSize, "JFK", &route);

    for (int left = 0, right = route.size - 1; left < right; left++, right--) {
        char* temp = route.items[left];
        route.items[left] = route.items[right];
        route.items[right] = temp;
    }

    for (int index = 0; index < graphSize; index++) {
        free(graph[index].destinations);
    }

    *returnSize = route.size;
    return route.items;
}
