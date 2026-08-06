<?php

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function modifyString($s) {
        $chars = str_split($s);
        $n = count($chars);
        for ($i = 0; $i < $n; $i++) {
            if ($chars[$i] !== '?') {
                continue;
            }
            foreach (['a', 'b', 'c'] as $c) {
                $leftOk = ($i === 0 || $chars[$i - 1] !== $c);
                $rightOk = ($i + 1 === $n || $chars[$i + 1] !== $c);
                if ($leftOk && $rightOk) {
                    $chars[$i] = $c;
                    break;
                }
            }
        }
        return implode('', $chars);
    }
}
