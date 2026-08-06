<?php
class Solution {
    function minJumps($arr) {
        $n = count($arr);
        $positions = [];
        for ($i = 0; $i < $n; $i++) $positions[$arr[$i]][] = $i;
        $queue = [0];
        $seen = [0 => true];
        $steps = 0;
        while ($queue) {
            $size = count($queue);
            for ($s = 0; $s < $size; $s++) {
                $i = array_shift($queue);
                if ($i === $n - 1) return $steps;
                $next = $positions[$arr[$i]] ?? [];
                unset($positions[$arr[$i]]);
                $next[] = $i - 1;
                $next[] = $i + 1;
                foreach ($next as $j) {
                    if ($j >= 0 && $j < $n && !isset($seen[$j])) {
                        $seen[$j] = true;
                        $queue[] = $j;
                    }
                }
            }
            $steps++;
        }
        return -1;
    }
}
