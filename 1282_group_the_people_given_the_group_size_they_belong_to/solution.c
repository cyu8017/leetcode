// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

#include <stdlib.h>
#include <string.h>

int** groupThePeople(int* groupSizes, int groupSizesSize, int* returnSize, int** returnColumnSizes) {
    int** pending[1001];
    int pendingSize[1001] = {0};
    int** result = (int**)malloc((size_t)groupSizesSize * sizeof(int*));
    int count = 0;
    for (int person = 0; person < groupSizesSize; person++) {
        int size = groupSizes[person];
        if (!pending[size]) pending[size] = (int**)malloc((size_t)size * sizeof(int*));
        pending[size][pendingSize[size]] = (int*)malloc(sizeof(int));
        pending[size][pendingSize[size]][0] = person;
        pendingSize[size]++;
        if (pendingSize[size] == size) {
            result[count] = (int*)malloc((size_t)size * sizeof(int));
            for (int i = 0; i < size; i++) result[count][i] = pending[size][i][0];
            for (int i = 0; i < size; i++) free(pending[size][i]);
            pendingSize[size] = 0;
            count++;
        }
    }
    for (int i = 0; i <= 1000; i++) free(pending[i]);
    for (int i = 0; i < count; i++) {
        for (int j = i + 1; j < count; j++) {
            int si = groupSizes[result[i][0]], sj = groupSizes[result[j][0]];
            int swap = 0;
            if (si != sj) swap = si > sj;
            else {
                for (int k = 0; k < si; k++) {
                    if (result[i][k] != result[j][k]) {
                        swap = result[i][k] > result[j][k];
                        break;
                    }
                }
            }
            if (swap) {
                int* tmp = result[i];
                result[i] = result[j];
                result[j] = tmp;
            }
        }
    }
    *returnColumnSizes = (int*)malloc((size_t)count * sizeof(int));
    for (int i = 0; i < count; i++) (*returnColumnSizes)[i] = groupSizes[result[i][0]];
    *returnSize = count;
    return result;
}
