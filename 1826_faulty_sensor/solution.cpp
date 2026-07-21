// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

#include <vector>

class Solution {
public:
    int badSensor(std::vector<int>& sensor1, std::vector<int>& sensor2) {
        if (sensor1 == sensor2) {
            return -1;
        }
        bool sensor1Bad = isDefective(sensor2, sensor1);
        bool sensor2Bad = isDefective(sensor1, sensor2);
        if (sensor1Bad && sensor2Bad) {
            return -1;
        }
        if (sensor1Bad) {
            return 1;
        }
        if (sensor2Bad) {
            return 2;
        }
        return -1;
    }

private:
    bool isDefective(const std::vector<int>& correct, const std::vector<int>& faulty) {
        int n = static_cast<int>(correct.size());
        int i = 0;
        while (i < n && correct[i] == faulty[i]) {
            ++i;
        }
        if (i == n) {
            return false;
        }
        int j = i;
        while (j < n - 1 && correct[j + 1] == faulty[j]) {
            ++j;
        }
        return j == n - 1;
    }
};
