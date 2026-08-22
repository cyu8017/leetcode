// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

int leastInterval(char* tasks, int tasksSize, int n) {
    int freq[26] = {0};
    int maxFreq = 0;
    for (int i = 0; i < tasksSize; i++) {
        int idx = tasks[i] - 'A';
        freq[idx]++;
        if (freq[idx] > maxFreq) {
            maxFreq = freq[idx];
        }
    }
    int maxCount = 0;
    for (int i = 0; i < 26; i++) {
        if (freq[i] == maxFreq) {
            maxCount++;
        }
    }
    int candidate = (maxFreq - 1) * (n + 1) + maxCount;
    return candidate > tasksSize ? candidate : tasksSize;
}
