// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

import java.util.Arrays;

class Solution {
    public int badSensor(int[] sensor1, int[] sensor2) {
        if (Arrays.equals(sensor1, sensor2)) {
            return -1;
        }

        boolean sensor1Bad = isDefective(sensor2, sensor1);
        boolean sensor2Bad = isDefective(sensor1, sensor2);

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

    private boolean isDefective(int[] correct, int[] faulty) {
        int n = correct.length;
        int i = 0;
        while (i < n && correct[i] == faulty[i]) {
            i++;
        }
        if (i == n) {
            return false;
        }

        int j = i;
        while (j < n - 1 && correct[j + 1] == faulty[j]) {
            j++;
        }
        return j == n - 1;
    }
}
