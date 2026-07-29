// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

#include <string.h>

int getMaxRepetitions(char* s1, int n1, char* s2, int n2) {
    int s2Len = (int)strlen(s2);
    if (s2Len == 0) {
        return 0;
    }

    int index = 0;
    int s2Count = 0;
    int recordIndex[128];
    int recordRepeat[128];
    int recordCount[128];
    int recordSize = 0;

    for (int repeat = 0; repeat < n1; repeat++) {
        for (int i = 0; s1[i]; i++) {
            if (s1[i] == s2[index]) {
                index++;
                if (index == s2Len) {
                    index = 0;
                    s2Count++;
                }
            }
        }

        int found = -1;
        for (int r = 0; r < recordSize; r++) {
            if (recordIndex[r] == index) {
                found = r;
                break;
            }
        }
        if (found >= 0) {
            int previousRepeat = recordRepeat[found];
            int previousCount = recordCount[found];
            int cycle = repeat - previousRepeat;
            int countCycle = s2Count - previousCount;
            int remaining = n1 - repeat - 1;
            s2Count += (remaining / cycle) * countCycle;
            repeat += (remaining / cycle) * cycle;
            if (repeat >= n1 - 1) {
                break;
            }
        }
        recordIndex[recordSize] = index;
        recordRepeat[recordSize] = repeat;
        recordCount[recordSize] = s2Count;
        recordSize++;
    }

    return s2Count / n2;
}
