// LeetCode 0018 - 4Sum
// https://leetcode.com/problems/4sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[][]
     */
    function fourSum($nums, $target) {
        sort($nums);
        $result = [];
        $n = count($nums);

        for ($i = 0; $i < $n - 3; $i++) {
            if ($i > 0 && $nums[$i] === $nums[$i - 1]) {
                continue;
            }

            for ($j = $i + 1; $j < $n - 2; $j++) {
                if ($j > $i + 1 && $nums[$j] === $nums[$j - 1]) {
                    continue;
                }

                $left = $j + 1;
                $right = $n - 1;
                while ($left < $right) {
                    $total = $nums[$i] + $nums[$j] + $nums[$left] + $nums[$right];
                    if ($total === $target) {
                        $result[] = [$nums[$i], $nums[$j], $nums[$left], $nums[$right]];
                        while ($left < $right && $nums[$left] === $nums[$left + 1]) {
                            $left++;
                        }
                        while ($left < $right && $nums[$right] === $nums[$right - 1]) {
                            $right--;
                        }
                        $left++;
                        $right--;
                    } elseif ($total < $target) {
                        $left++;
                    } else {
                        $right--;
                    }
                }
            }
        }

        return $result;
    }
}
