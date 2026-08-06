<?php
class Solution {
    function constrainedSubsetSum($nums, $k) {
        $n = count($nums);
        $best = $nums;
        $queue = [];
        for ($i = 0; $i < $n; $i++) {
            while ($queue && $queue[0] < $i - $k) array_shift($queue);
            $best[$i] = $nums[$i] + max(0, $queue ? $best[$queue[0]] : 0);
            while ($queue && $best[$queue[count($queue) - 1]] <= $best[$i]) array_pop($queue);
            $queue[] = $i;
        }
        return max($best);
    }
}
