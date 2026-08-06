<?php

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minSwaps($grid) {
        $zeros = [];
        foreach ($grid as $row) {
            $count = 0;
            for ($i = count($row) - 1; $i >= 0; $i--) {
                if ($row[$i]) {
                    break;
                }
                $count++;
            }
            $zeros[] = $count;
        }
        $answer = 0;
        $n = count($grid);
        for ($i = 0; $i < $n; $i++) {
            $required = $n - $i - 1;
            $j = $i;
            while ($j < $n && $zeros[$j] < $required) {
                $j++;
            }
            if ($j === $n) {
                return -1;
            }
            $answer += $j - $i;
            $chosen = $zeros[$j];
            for ($t = $j; $t > $i; $t--) {
                $zeros[$t] = $zeros[$t - 1];
            }
            $zeros[$i] = $chosen;
        }
        return $answer;
    }
}
