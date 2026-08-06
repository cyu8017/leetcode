<?php

class Solution {
    /**
     * @param String[] $dict
     * @return Boolean
     */
    function differByOne($dict) {
        $seen = [];
        foreach ($dict as $word) {
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $pattern = substr($word, 0, $i) . '*' . substr($word, $i + 1);
                if (isset($seen[$pattern])) {
                    return true;
                }
                $seen[$pattern] = true;
            }
        }
        return false;
    }
}
