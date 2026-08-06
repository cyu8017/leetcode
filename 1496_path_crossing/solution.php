<?php
class Solution {
    function isPathCrossing($path) {
        $x = 0;
        $y = 0;
        $seen = ["0,0" => true];
        $move = ["N" => [0, 1], "S" => [0, -1], "E" => [1, 0], "W" => [-1, 0]];
        for ($i = 0; $i < strlen($path); $i++) {
            [$dx, $dy] = $move[$path[$i]];
            $x += $dx;
            $y += $dy;
            $key = "$x,$y";
            if (isset($seen[$key])) return true;
            $seen[$key] = true;
        }
        return false;
    }
}
