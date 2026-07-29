// LeetCode 1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool is_subset(char** a, int an, char** b, int bn) {
    for (int i = 0; i < an; i++) {
        bool found = false;
        for (int j = 0; j < bn; j++) if (strcmp(a[i], b[j]) == 0) { found = true; break; }
        if (!found) return false;
    }
    return true;
}

int* peopleIndexes(char*** favoriteCompanies, int favoriteCompaniesSize, int* favoriteCompaniesColSize, int* returnSize) {
    int* ans = (int*)malloc(favoriteCompaniesSize * sizeof(int));
    int an = 0;
    for (int i = 0; i < favoriteCompaniesSize; i++) {
        bool subset = false;
        for (int j = 0; j < favoriteCompaniesSize; j++) {
            if (i != j && is_subset(favoriteCompanies[i], favoriteCompaniesColSize[i],
                                    favoriteCompanies[j], favoriteCompaniesColSize[j])) {
                subset = true; break;
            }
        }
        if (!subset) ans[an++] = i;
    }
    *returnSize = an;
    return ans;
}
