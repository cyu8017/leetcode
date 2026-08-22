// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int minMutation(char* startGene, char* endGene, char** bank, int bankSize) {
    if (strcmp(startGene, endGene) == 0) {
        return 0;
    }

    bool endInBank = false;
    for (int i = 0; i < bankSize; i++) {
        if (strcmp(bank[i], endGene) == 0) {
            endInBank = true;
            break;
        }
    }
    if (!endInBank) {
        return -1;
    }

    char** queue = (char**)malloc((size_t)(bankSize + 1) * sizeof(char*));
    int* stepsArr = (int*)malloc((size_t)(bankSize + 1) * sizeof(int));
    bool* visited = (bool*)calloc((size_t)bankSize, sizeof(bool));
    int head = 0;
    int tail = 0;
    queue[tail] = startGene;
    stepsArr[tail++] = 0;

    const char* genes = "ACGT";

    while (head < tail) {
        char* gene = queue[head];
        int steps = stepsArr[head++];
        if (strcmp(gene, endGene) == 0) {
            free(queue);
            free(stepsArr);
            free(visited);
            return steps;
        }

        char candidate[9];
        strcpy(candidate, gene);
        for (int index = 0; index < 8; index++) {
            char original = candidate[index];
            for (int g = 0; g < 4; g++) {
                if (genes[g] == original) {
                    continue;
                }
                candidate[index] = genes[g];
                for (int b = 0; b < bankSize; b++) {
                    if (!visited[b] && strcmp(bank[b], candidate) == 0) {
                        visited[b] = true;
                        queue[tail] = bank[b];
                        stepsArr[tail++] = steps + 1;
                    }
                }
            }
            candidate[index] = original;
        }
    }

    free(queue);
    free(stepsArr);
    free(visited);
    return -1;
}
