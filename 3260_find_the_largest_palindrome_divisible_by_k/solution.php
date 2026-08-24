<?php
// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

class Solution {
    function largestPalindrome($n, $k) {
        $digits = array_fill(0, $n, '9');
        $half = intdiv($n + 1, 2);
        switch ($k) {
            case 1:
            case 3:
            case 9:
                return implode('', $digits);
            case 2:
                $digits[0] = $digits[$n - 1] = '8';
                return implode('', $digits);
            case 4:
                if ($n === 1) return '8';
                $digits[0] = $digits[1] = $digits[$n - 1] = $digits[$n - 2] = '8';
                return implode('', $digits);
            case 5:
                $digits[0] = $digits[$n - 1] = '5';
                return implode('', $digits);
            case 8:
                if ($n <= 2) return str_repeat('8', $n);
                $digits[0] = $digits[1] = $digits[2] = '8';
                $digits[$n - 1] = $digits[$n - 2] = $digits[$n - 3] = '8';
                return implode('', $digits);
            case 6:
                if ($n === 1) return '6';
                $digits[0] = $digits[$n - 1] = '8';
                $sum = 16 + 9 * ($n - 2);
                $need = $sum % 3;
                if ($need !== 0) {
                    $pos = $half - 1;
                    $digits[$pos] = chr(ord($digits[$pos]) - $need);
                    if ($n % 2 === 0 || $pos !== $n - 1 - $pos) $digits[$n - 1 - $pos] = $digits[$pos];
                }
                return implode('', $digits);
            case 7:
                return $this->largestPal7($n);
            default:
                return implode('', $digits);
        }
    }

    private function mod7($s) {
        $r = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) $r = ($r * 10 + (ord($s[$i]) - 48)) % 7;
        return $r;
    }

    private function largestPal7($n) {
        $halfLen = intdiv($n + 1, 2);
        $half = array_fill(0, $halfLen, '9');
        for (;;) {
            $pal = array_fill(0, $n, '0');
            for ($i = 0; $i < $halfLen; $i++) $pal[$i] = $half[$i];
            for ($i = 0; $i < intdiv($n, 2); $i++) $pal[$n - 1 - $i] = $pal[$i];
            if ($this->mod7(implode('', $pal)) === 0) return implode('', $pal);
            $idx = $halfLen - 1;
            while ($idx >= 0 && $half[$idx] === '0') { $half[$idx] = '9'; $idx--; }
            if ($idx < 0) break;
            $half[$idx] = chr(ord($half[$idx]) - 1);
        }
        return '';
    }
}
