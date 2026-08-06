<?php
class Solution {
    /**
     * @param String[] $nums
     * @return String
     */
    function findDifferentBinaryString($nums) {
        $s = array_flip($nums);
        $n = count($nums);
        $preferred = [
            '11', '101', '00', '10', '01',
            '000', '001', '010', '011', '100', '110', '111',
        ];
        foreach ($preferred as $cand) {
            if (strlen($cand) === $n && !isset($s[$cand])) {
                return $cand;
            }
        }
        $limit = 1 << $n;
        for ($i = 0; $i < $limit; $i++) {
            $cand = str_pad(decbin($i), $n, '0', STR_PAD_LEFT);
            if (!isset($s[$cand])) {
                return $cand;
            }
        }
        return str_repeat('0', $n);
    }
}
