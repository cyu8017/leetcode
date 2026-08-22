// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

#include <stdbool.h>

bool knows(int a, int b) {
    return false;
}

int findCelebrity(int n) {
    int candidate = 0;
    for (int person = 1; person < n; person++) {
        if (knows(candidate, person)) {
            candidate = person;
        }
    }
    for (int person = 0; person < n; person++) {
        if (person == candidate) {
            continue;
        }
        if (knows(candidate, person) || !knows(person, candidate)) {
            return -1;
        }
    }
    return candidate;
}
