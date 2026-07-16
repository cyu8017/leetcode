// LeetCode 0152 - Maximum Product Subarray
// https://leetcode.com/problems/maximum-product-subarray/

class Solution {
    function maxProduct(array $nums): int {
        $best = $maxProduct = $minProduct = $nums[0];
        for ($i = 1; $i < count($nums); $i++) {
            $number = $nums[$i];
            $candidates = [$number, $maxProduct * $number, $minProduct * $number];
            $maxProduct = max($candidates);
            $minProduct = min($candidates);
            $best = max($best, $maxProduct);
        }
        return $best;
    }
}