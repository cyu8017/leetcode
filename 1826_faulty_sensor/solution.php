<?php
// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

class Solution {
    /**
     * @param Integer[] $sensor1
     * @param Integer[] $sensor2
     * @return Integer
     */
    function badSensor($sensor1, $sensor2) {
        if ($sensor1 === $sensor2) {
            return -1;
        }

        $sensor1Bad = $this->isDefective($sensor2, $sensor1);
        $sensor2Bad = $this->isDefective($sensor1, $sensor2);

        if ($sensor1Bad && $sensor2Bad) {
            return -1;
        }
        if ($sensor1Bad) {
            return 1;
        }
        if ($sensor2Bad) {
            return 2;
        }
        return -1;
    }

    /**
     * @param Integer[] $correct
     * @param Integer[] $faulty
     * @return Boolean
     */
    private function isDefective($correct, $faulty) {
        $n = count($correct);
        $i = 0;
        while ($i < $n && $correct[$i] === $faulty[$i]) {
            $i++;
        }
        if ($i === $n) {
            return false;
        }

        $j = $i;
        while ($j < $n - 1 && $correct[$j + 1] === $faulty[$j]) {
            $j++;
        }
        return $j === $n - 1;
    }
}
