<?php
// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

class Solution {
    /**
     * @param Integer[] $releaseTimes
     * @param String $keysPressed
     * @return String
     */
    function slowestKey($releaseTimes, $keysPressed) {
        $bestDur = $releaseTimes[0];
        $bestKey = $keysPressed[0];
        $n = count($releaseTimes);
        for ($i = 1; $i < $n; $i++) {
            $duration = $releaseTimes[$i] - $releaseTimes[$i - 1];
            if ($duration > $bestDur || ($duration === $bestDur && $keysPressed[$i] > $bestKey)) {
                $bestDur = $duration;
                $bestKey = $keysPressed[$i];
            }
        }
        return $bestKey;
    }
}
