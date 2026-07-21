// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

public class Solution {
    public int BadSensor(int[] sensor1, int[] sensor2) {
        bool equal = true;
        for (int i = 0; i < sensor1.Length; i++) {
            if (sensor1[i] != sensor2[i]) { equal = false; break; }
        }
        if (equal) return -1;

        bool IsDefective(int[] correct, int[] faulty) {
            int n = correct.Length;
            int i = 0;
            while (i < n && correct[i] == faulty[i]) i++;
            if (i == n) return false;
            int j = i;
            while (j < n - 1 && correct[j + 1] == faulty[j]) j++;
            return j == n - 1;
        }

        bool sensor1Bad = IsDefective(sensor2, sensor1);
        bool sensor2Bad = IsDefective(sensor1, sensor2);
        if (sensor1Bad && sensor2Bad) return -1;
        if (sensor1Bad) return 1;
        if (sensor2Bad) return 2;
        return -1;
    }
}
