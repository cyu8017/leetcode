<?php
// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

class Solution {
    /**
     * @param String $ring
     * @param String $key
     * @return Integer
     */
    function findRotateSteps($ring, $key) {
        return $this->find_rotate_steps($ring, $key);
    }

    /**
     * @param String $ring
     * @param String $key
     * @return Integer
     */
    function find_rotate_steps($ring, $key) {
        $positions = [];
        $ringLength = strlen($ring);
        for ($index = 0; $index < $ringLength; $index++) {
            $char = $ring[$index];
            if (!isset($positions[$char])) {
                $positions[$char] = [];
            }
            $positions[$char][] = $index;
        }

        $memo = [];
        $dp = function ($ringIndex, $keyIndex) use (&$dp, $key, $ringLength, $positions, &$memo) {
            if ($keyIndex === strlen($key)) {
                return 0;
            }

            $state = $ringIndex . ',' . $keyIndex;
            if (array_key_exists($state, $memo)) {
                return $memo[$state];
            }

            $best = PHP_INT_MAX;
            foreach ($positions[$key[$keyIndex]] as $pos) {
                $clockwise = ($pos - $ringIndex + $ringLength) % $ringLength;
                $counter = ($ringIndex - $pos + $ringLength) % $ringLength;
                $steps = min($clockwise, $counter) + 1;
                $best = min($best, $steps + $dp($pos, $keyIndex + 1));
            }

            $memo[$state] = $best;
            return $best;
        };

        return $dp(0, 0);
    }
}
