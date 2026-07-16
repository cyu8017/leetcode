<?php
// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

class Solution {
    /**
     * @param string $s
     * @param int $k
     * @return string
     */
    function licenseKeyFormatting($s, $k) {
        return $this->license_key_formatting($s, $k);
    }

    /**
     * @param string $s
     * @param int $k
     * @return string
     */
    function license_key_formatting($s, $k) {
        $chars = [];
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            $ch = $s[$index];
            if ($ch !== '-') {
                $chars[] = strtoupper($ch);
            }
        }
        if (count($chars) === 0) {
            return '';
        }
        $firstLen = count($chars) % $k;
        if ($firstLen === 0) {
            $firstLen = $k;
        }
        $parts = [implode('', array_slice($chars, 0, $firstLen))];
        for ($index = $firstLen; $index < count($chars); $index += $k) {
            $parts[] = implode('', array_slice($chars, $index, $k));
        }
        return implode('-', $parts);
    }
}
