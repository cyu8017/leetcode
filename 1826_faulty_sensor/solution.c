// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

#include <stdbool.h>

static bool isDefective(int* correct, int* faulty, int n) {
    int i = 0;
    while (i < n && correct[i] == faulty[i]) i++;
    if (i == n) return false;
    int j = i;
    while (j < n - 1 && correct[j + 1] == faulty[j]) j++;
    return j == n - 1;
}

int badSensor(int* sensor1, int sensor1Size, int* sensor2, int sensor2Size) {
    (void)sensor2Size;
    int n = sensor1Size;
    bool same = true;
    for (int i = 0; i < n; i++) {
        if (sensor1[i] != sensor2[i]) {
            same = false;
            break;
        }
    }
    if (same) return -1;

    bool sensor1Bad = isDefective(sensor2, sensor1, n);
    bool sensor2Bad = isDefective(sensor1, sensor2, n);
    if (sensor1Bad && sensor2Bad) return -1;
    if (sensor1Bad) return 1;
    if (sensor2Bad) return 2;
    return -1;
}
