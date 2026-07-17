// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

double averageWaitingTime(int** customers, int customersSize, int* customersColSize) {
    long long current = 0;
    long long total = 0;
    for (int i = 0; i < customersSize; i++) {
        long long arrival = customers[i][0];
        long long cook = customers[i][1];
        current = (current > arrival ? current : arrival) + cook;
        total += current - arrival;
    }
    return (double)total / customersSize;
}
