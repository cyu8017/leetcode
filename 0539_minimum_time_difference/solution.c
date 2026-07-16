// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

#include <stdlib.h>
#include <string.h>

static int compare_ints(const void* left, const void* right) {
    const int a = *(const int*)left;
    const int b = *(const int*)right;
    return a - b;
}

static int to_minutes(const char* time) {
    const int hour = (time[0] - '0') * 10 + (time[1] - '0');
    const int minute = (time[3] - '0') * 10 + (time[4] - '0');
    return hour * 60 + minute;
}

int findMinDifference(char** timePoints, int timePointsSize) {
    int* minutes = (int*)malloc((size_t)timePointsSize * sizeof(int));
    if (!minutes) {
        return 0;
    }

    for (int index = 0; index < timePointsSize; index++) {
        minutes[index] = to_minutes(timePoints[index]);
    }

    qsort(minutes, (size_t)timePointsSize, sizeof(int), compare_ints);

    int best = minutes[timePointsSize - 1] - minutes[0];
    for (int index = 1; index < timePointsSize; index++) {
        const int diff = minutes[index] - minutes[index - 1];
        if (diff < best) {
            best = diff;
        }
    }

    const int wrap = 24 * 60 - minutes[timePointsSize - 1] + minutes[0];
    if (wrap < best) {
        best = wrap;
    }

    free(minutes);
    return best;
}
