<?php

class Solution {
    /**
     * @param String $num
     * @param Integer[] $change
     * @return String
     */
    function maximumNumber($num, $change) {
        $chars = str_split($num);
        $started = false;
        $n = count($chars);
        for ($i = 0; $i < $n; $i++) {
            $d = (int)$chars[$i];
            $mapped = $change[$d];
            if ($mapped > $d) {
                $chars[$i] = (string)$mapped;
                $started = true;
            } elseif ($mapped < $d && $started) {
                break;
            }
        }
        return implode('', $chars);
    }
}
