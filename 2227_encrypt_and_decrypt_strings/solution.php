<?php
// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter {
    private $enc = [];
    private $cnt = [];

    function __construct($keys, $values, $dictionary) {
        for ($i = 0; $i < count($keys); $i++) $this->enc[$keys[$i]] = $values[$i];
        foreach ($dictionary as $w) {
            $e = $this->encrypt($w);
            $this->cnt[$e] = ($this->cnt[$e] ?? 0) + 1;
        }
    }

    function encrypt($word1) {
        $b = '';
        $n = strlen($word1);
        for ($i = 0; $i < $n; $i++) {
            $c = $word1[$i];
            if (!isset($this->enc[$c])) return '';
            $b .= $this->enc[$c];
        }
        return $b;
    }

    function decrypt($word2) {
        return $this->cnt[$word2] ?? 0;
    }
}
