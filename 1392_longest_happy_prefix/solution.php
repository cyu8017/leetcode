<?php
class Solution {
    function longestPrefix($s) {
        $n = strlen($s);
        if (!$n) return "";
        $pi = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            $j = $pi[$i - 1];
            while ($j && $s[$i] !== $s[$j]) $j = $pi[$j - 1];
            if ($s[$i] === $s[$j]) $j++;
            $pi[$i] = $j;
        }
        return substr($s, 0, $pi[$n - 1]);
    }
}
