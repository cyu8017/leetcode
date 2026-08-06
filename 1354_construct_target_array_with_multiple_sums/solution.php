<?php
class Solution {
    function isPossible($target) {
        if (count($target) === 1) return $target[0] === 1;
        $h = new SplMaxHeap();
        $total = 0;
        foreach ($target as $x) {
            $h->insert($x);
            $total += $x;
        }
        while (true) {
            $x = $h->extract();
            $rest = $total - $x;
            if ($x === 1 || $rest === 1) return true;
            if ($rest === 0 || $x <= $rest) return false;
            $prev = $x % $rest;
            if ($prev === 0) return false;
            $total = $rest + $prev;
            $h->insert($prev);
        }
    }
}
