// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    boolean rotationMatches(int[] block, int[] target) {
        int k = block.length;
        int[] prefix = new int[k];
        for (int i = 1; i < k; i++) {
            int j = prefix[i - 1];
            while (j > 0 && target[i] != target[j]) j = prefix[j - 1];
            if (target[i] == target[j]) j++;
            prefix[i] = j;
        }
        int matched = 0;
        for (int i = 0; i < 2 * k - 1; i++) {
            int x = block[i % k];
            while (matched > 0 && x != target[matched]) matched = prefix[matched - 1];
            if (x == target[matched]) matched++;
            if (matched == k) return true;
        }
        return false;
    }

    public int sumOfSortableIntegers(int[] nums) {
        int n = nums.length;
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        List<Integer> divisors = new ArrayList<>();
        for (int d = 1; d * d <= n; d++) {
            if (n % d == 0) {
                divisors.add(d);
                if (d * d != n) divisors.add(n / d);
            }
        }
        int answer = 0;
        for (int k : divisors) {
            boolean ok = true;
            for (int start = 0; start < n; start += k) {
                int[] block = Arrays.copyOfRange(nums, start, start + k);
                int[] target = Arrays.copyOfRange(sorted, start, start + k);
                if (!rotationMatches(block, target)) { ok = false; break; }
            }
            if (ok) answer += k;
        }
        return answer;
    }
}
