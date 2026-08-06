<?php
class Solution {
    function findTheDistanceValue($arr1, $arr2, $d) {
        sort($arr2);
        $ans = 0;
        foreach ($arr1 as $x) {
            $lo = 0;
            $hi = count($arr2);
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($arr2[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ok = true;
            if ($lo < count($arr2) && abs($arr2[$lo] - $x) <= $d) $ok = false;
            if ($lo > 0 && abs($arr2[$lo - 1] - $x) <= $d) $ok = false;
            if ($ok) $ans++;
        }
        return $ans;
    }
}
