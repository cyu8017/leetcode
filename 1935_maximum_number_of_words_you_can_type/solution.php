<?php
class Solution {
    /**
     * @param String $text
     * @param String $brokenLetters
     * @return Integer
     */
    function canBeTypedWords($text, $brokenLetters) {
        $broken = [];
        $blen = strlen($brokenLetters);
        for ($i = 0; $i < $blen; $i++) {
            $broken[$brokenLetters[$i]] = true;
        }
        $ans = 0;
        foreach (explode(' ', $text) as $w) {
            $ok = true;
            $wlen = strlen($w);
            for ($i = 0; $i < $wlen; $i++) {
                if (isset($broken[$w[$i]])) {
                    $ok = false;
                    break;
                }
            }
            if ($ok) {
                $ans++;
            }
        }
        return $ans;
    }
}
