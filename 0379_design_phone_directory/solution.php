<?php
// LeetCode 0379 - Design Phone Directory
// https://leetcode.com/problems/design-phone-directory/

class PhoneDirectory {
    /** @var array<int, bool> */
    private array $available = [];

    /**
     * @param Integer $maxNumbers
     */
    function __construct($maxNumbers) {
        for ($index = 0; $index < $maxNumbers; $index++) {
            $this->available[$index] = true;
        }
    }

    /**
     * @return Integer
     */
    function get() {
        if (count($this->available) === 0) {
            return -1;
        }

        $number = min(array_keys($this->available));
        unset($this->available[$number]);
        return $number;
    }

    /**
     * @param Integer $number
     * @return Boolean
     */
    function check($number) {
        return isset($this->available[$number]);
    }

    /**
     * @param Integer $number
     * @return void
     */
    function release($number) {
        $this->available[$number] = true;
    }
}
