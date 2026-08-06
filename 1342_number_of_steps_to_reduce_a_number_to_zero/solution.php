<?php
class Solution {
    function numberOfSteps($num) {
        $steps = 0;
        while ($num) {
            $num = $num % 2 === 0 ? intdiv($num, 2) : $num - 1;
            $steps++;
        }
        return $steps;
    }
}
