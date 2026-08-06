<?php
class Solution {
    /**
     * @param String $num
     * @return Boolean
     */
    function sumGame($num) {
        $n = strlen($num);
        $half = intdiv($n, 2);
        return $this->score(substr($num, 0, $half)) !== $this->score(substr($num, $half));
    }

    private function score($s) {
        $q = 0;
        $dig = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '?') {
                $q++;
            } else {
                $dig += (int)$s[$i];
            }
        }
        return $dig * 2 + $q * 9;
    }
}
