<?php
// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

class Solution {
    /**
     * @param string $s1
     * @param int $n1
     * @param string $s2
     * @param int $n2
     * @return int
     */
    function getMaxRepetitions($s1, $n1, $s2, $n2) {
        return $this->get_max_repetitions($s1, $n1, $s2, $n2);
    }

    /**
     * @param string $s1
     * @param int $n1
     * @param string $s2
     * @param int $n2
     * @return int
     */
    function get_max_repetitions($s1, $n1, $s2, $n2) {
        if ($s2 === '') {
            return 0;
        }

        $index = 0;
        $s2Count = 0;
        $record = [];

        for ($repeat = 0; $repeat < $n1; $repeat++) {
            $length = strlen($s1);
            for ($position = 0; $position < $length; $position++) {
                if ($s1[$position] === $s2[$index]) {
                    $index++;
                    if ($index === strlen($s2)) {
                        $index = 0;
                        $s2Count++;
                    }
                }
            }

            if (array_key_exists($index, $record)) {
                [$previousRepeat, $previousCount] = $record[$index];
                $cycle = $repeat - $previousRepeat;
                $countCycle = $s2Count - $previousCount;
                $remaining = $n1 - $repeat - 1;
                $s2Count += intdiv($remaining, $cycle) * $countCycle;
                if ($repeat + intdiv($remaining, $cycle) * $cycle >= $n1 - 1) {
                    break;
                }
            }
            $record[$index] = [$repeat, $s2Count];
        }

        return intdiv($s2Count, $n2);
    }
}
