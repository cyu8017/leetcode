// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String getPermutation(int n, int k) {
        List<Integer> numbers = new ArrayList<>();
        int[] factorials = new int[n];
        factorials[0] = 1;

        for (int i = 1; i < n; i++) {
            numbers.add(i);
            factorials[i] = factorials[i - 1] * i;
        }
        numbers.add(n);

        k--;
        StringBuilder result = new StringBuilder();

        for (int i = n - 1; i >= 0; i--) {
            int index = k / factorials[i];
            result.append(numbers.get(index));
            numbers.remove(index);
            k %= factorials[i];
        }

        return result.toString();
    }
}
