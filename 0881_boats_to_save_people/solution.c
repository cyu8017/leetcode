// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

int numRescueBoats(int* people, int peopleSize, int limit) {
    qsort(people, (size_t)peopleSize, sizeof(int), cmp_int);
    int i = 0, j = peopleSize - 1, boats = 0;
    while (i <= j) {
        if (people[i] + people[j] <= limit) i++;
        j--;
        boats++;
    }
    return boats;
}
