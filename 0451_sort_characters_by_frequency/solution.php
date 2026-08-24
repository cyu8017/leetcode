<?php
// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

class Solution {
    /**
     * @param string $s
     * @return string
     */
    function frequencySort($s) {
        return $this->frequency_sort($s);
    }

    /**
     * @param string $s
     * @return string
     */
    function frequency_sort($s) {
        $counts = [];
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            $ch = $s[$index];
            if (!array_key_exists($ch, $counts)) {
                $counts[$ch] = 0;
            }
            $counts[$ch]++;
        }

        $entries = [];
        foreach ($counts as $ch => $count) {
            $entries[] = [$ch, $count];
        }
        usort($entries, function ($left, $right) {
            if ($left[1] !== $right[1]) {
                return $right[1] <=> $left[1];
            }
            return $left[0] <=> $right[0];
        });

        $result = '';
        foreach ($entries as [$ch, $count]) {
            $result .= str_repeat($ch, $count);
        }
        return $result;
    }
}
