<?php
class Solution {
    function angleClock($hour, $minutes) {
        $difference = abs(($hour % 12) * 30 + $minutes * 0.5 - $minutes * 6);
        return min($difference, 360 - $difference);
    }
}
