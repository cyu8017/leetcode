<?php
// LeetCode 0354 - Russian Doll Envelopes
// https://leetcode.com/problems/russian-doll-envelopes/

class Solution {
    /**
     * @param Integer[][] $envelopes
     * @return Integer
     */
    function maxEnvelopes($envelopes) {
        return $this->max_envelopes($envelopes);
    }

    /**
     * @param Integer[][] $envelopes
     * @return Integer
     */
    function max_envelopes($envelopes) {
        usort($envelopes, function ($left, $right) {
            if ($left[0] === $right[0]) {
                return $right[1] <=> $left[1];
            }
            return $left[0] <=> $right[0];
        });

        $tails = [];
        foreach ($envelopes as $envelope) {
            $height = $envelope[1];
            $index = $this->bisectLeft($tails, $height);
            if ($index === count($tails)) {
                $tails[] = $height;
            } else {
                $tails[$index] = $height;
            }
        }

        return count($tails);
    }

    /**
     * @param Integer[] $array
     * @param Integer $target
     * @return Integer
     */
    private function bisectLeft($array, $target) {
        $left = 0;
        $right = count($array);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($array[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }
}
