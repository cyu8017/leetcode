// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

#include <stdlib.h>

static int cmp3169(const void* a, const void* b) {
    int* const* aa = (int* const*)a;
    int* const* bb = (int* const*)b;
    return (*aa)[0] - (*bb)[0];
}

int countDays(int days, int** meetings, int meetingsSize, int* meetingsColSize) {
    (void)meetingsColSize;
    qsort(meetings, meetingsSize, sizeof(int*), cmp3169);
    int ans = 0, last = 0;
    for (int i = 0; i < meetingsSize; i++) {
        int st = meetings[i][0], ed = meetings[i][1];
        if (last < st) ans += st - last - 1;
        if (ed > last) last = ed;
    }
    ans += days - last;
    return ans;
}
