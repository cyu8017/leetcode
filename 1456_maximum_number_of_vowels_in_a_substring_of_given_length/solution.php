<?php
class Solution {
    function maxVowels($s, $k) {
        $vowels = ['a'=>1,'e'=>1,'i'=>1,'o'=>1,'u'=>1];
        $cur = 0;
        for ($i = 0; $i < $k; $i++) if (isset($vowels[$s[$i]])) $cur++;
        $ans = $cur;
        for ($i = $k; $i < strlen($s); $i++) {
            if (isset($vowels[$s[$i]])) $cur++;
            if (isset($vowels[$s[$i - $k]])) $cur--;
            $ans = max($ans, $cur);
        }
        return $ans;
    }
}
