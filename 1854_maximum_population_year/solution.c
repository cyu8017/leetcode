// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

int maximumPopulation(int** logs, int logsSize, int* logsColSize) {
    (void)logsColSize;
    int diff[101] = {0};
    for (int i = 0; i < logsSize; i++) {
        diff[logs[i][0] - 1950] += 1;
        diff[logs[i][1] - 1950] -= 1;
    }
    int bestYear = 1950;
    int bestPopulation = 0;
    int population = 0;
    for (int offset = 0; offset < 101; offset++) {
        population += diff[offset];
        if (population > bestPopulation) {
            bestPopulation = population;
            bestYear = 1950 + offset;
        }
    }
    return bestYear;
}
