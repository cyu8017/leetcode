// LeetCode 0134 - Gas Station
int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
    int total = 0, tank = 0, start = 0;
    for (int i = 0; i < gasSize; ++i) { int diff = gas[i] - cost[i]; total += diff; tank += diff; if (tank < 0) { tank = 0; start = i + 1; } }
    return total < 0 ? -1 : start;
}