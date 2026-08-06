<?php
// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

class MovieRentingSystem {
    private $price = [];
    private $available = [];
    private $rented = [];

    /**
     * @param Integer $n
     * @param Integer[][] $entries
     */
    function __construct($n, $entries) {
        foreach ($entries as $entry) {
            [$shop, $movie, $price] = $entry;
            $this->price["$shop,$movie"] = $price;
            if (!isset($this->available[$movie])) {
                $this->available[$movie] = [];
            }
            $this->insertAvailable($movie, $price, $shop);
        }
    }

    /**
     * @param Integer $movie
     * @return Integer[]
     */
    function search($movie) {
        $shops = [];
        if (!isset($this->available[$movie])) {
            return $shops;
        }
        $limit = min(5, count($this->available[$movie]));
        for ($i = 0; $i < $limit; $i++) {
            $shops[] = $this->available[$movie][$i][1];
        }
        return $shops;
    }

    /**
     * @param Integer $shop
     * @param Integer $movie
     * @return NULL
     */
    function rent($shop, $movie) {
        $price = $this->price["$shop,$movie"];
        $this->removeAvailable($movie, $price, $shop);
        $this->insertRented($price, $shop, $movie);
    }

    /**
     * @param Integer $shop
     * @param Integer $movie
     * @return NULL
     */
    function drop($shop, $movie) {
        $price = $this->price["$shop,$movie"];
        $this->removeRented($price, $shop, $movie);
        $this->insertAvailable($movie, $price, $shop);
    }

    /**
     * @return Integer[][]
     */
    function report() {
        $res = [];
        $limit = min(5, count($this->rented));
        for ($i = 0; $i < $limit; $i++) {
            $res[] = [$this->rented[$i][1], $this->rented[$i][2]];
        }
        return $res;
    }

    private function insertAvailable($movie, $price, $shop) {
        $item = [$price, $shop];
        $arr = &$this->available[$movie];
        $lo = 0;
        $hi = count($arr);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid][0] < $price || ($arr[$mid][0] === $price && $arr[$mid][1] < $shop)) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        array_splice($arr, $lo, 0, [$item]);
    }

    private function removeAvailable($movie, $price, $shop) {
        $arr = &$this->available[$movie];
        foreach ($arr as $i => $item) {
            if ($item[0] === $price && $item[1] === $shop) {
                array_splice($arr, $i, 1);
                return;
            }
        }
    }

    private function insertRented($price, $shop, $movie) {
        $item = [$price, $shop, $movie];
        $lo = 0;
        $hi = count($this->rented);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $cur = $this->rented[$mid];
            if ($cur[0] < $price
                || ($cur[0] === $price && $cur[1] < $shop)
                || ($cur[0] === $price && $cur[1] === $shop && $cur[2] < $movie)) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        array_splice($this->rented, $lo, 0, [$item]);
    }

    private function removeRented($price, $shop, $movie) {
        foreach ($this->rented as $i => $item) {
            if ($item[0] === $price && $item[1] === $shop && $item[2] === $movie) {
                array_splice($this->rented, $i, 1);
                return;
            }
        }
    }
}
