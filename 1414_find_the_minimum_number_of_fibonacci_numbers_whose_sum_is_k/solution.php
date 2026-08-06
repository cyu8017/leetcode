<?php
class Solution {
    function findMinFibonacciNumbers($k) {
        $fib = [1, 1];
        while ($fib[count($fib) - 1] < $k) $fib[] = $fib[count($fib) - 1] + $fib[count($fib) - 2];
        $answer = 0;
        for ($i = count($fib) - 1; $i >= 0; $i--) {
            if ($fib[$i] <= $k) {
                $k -= $fib[$i];
                $answer++;
            }
        }
        return $answer;
    }
}
