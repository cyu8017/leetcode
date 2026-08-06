<?php
class Solution {
    function numTimesAllBlue($flips) {
        $ans = 0;
        $mx = 0;
        foreach ($flips as $i => $x) {
            $mx = max($mx, $x);
            if ($mx === $i + 1) $ans++;
        }
        return $ans;
    }
}
