<?php
class Cashier {
    private $n;
    private $discount;
    private $price = [];
    private $count = 0;

    function __construct($n, $discount, $products, $prices) {
        $this->n = $n;
        $this->discount = $discount;
        foreach ($products as $i => $p) $this->price[$p] = $prices[$i];
        $this->count = 0;
    }

    function getBill($product, $amount) {
        $this->count++;
        $total = 0;
        foreach ($product as $i => $p) $total += $this->price[$p] * $amount[$i];
        if ($this->count % $this->n === 0) return $total * (100 - $this->discount) / 100.0;
        return floatval($total);
    }
}
