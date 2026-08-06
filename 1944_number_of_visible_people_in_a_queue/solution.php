<?php

class Solution {
    /**
     * @param Integer[] $heights
     * @return Integer[]
     */
    function canSeePersonsCount($heights) {
        $n = count($heights);
        $ans = array_fill(0, $n, 0);
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            $count = 0;
            while (!empty($stack) && $heights[$i] > $stack[count($stack) - 1]) {
                array_pop($stack);
                $count++;
            }
            if (!empty($stack)) {
                $count++;
            }
            $ans[$i] = $count;
            $stack[] = $heights[$i];
        }
        return $ans;
    }
}
