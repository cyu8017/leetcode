<?php

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maxUniqueSplit($s) {
        $used = [];
        $answer = 0;
        $n = strlen($s);

        $dfs = function ($i) use (&$dfs, &$used, &$answer, $s, $n) {
            if (count($used) + ($n - $i) <= $answer) {
                return;
            }
            if ($i === $n) {
                $answer = max($answer, count($used));
                return;
            }
            for ($j = $i + 1; $j <= $n; $j++) {
                $part = substr($s, $i, $j - $i);
                if (!isset($used[$part])) {
                    $used[$part] = true;
                    $dfs($j);
                    unset($used[$part]);
                }
            }
        };

        $dfs(0);
        return $answer;
    }
}
