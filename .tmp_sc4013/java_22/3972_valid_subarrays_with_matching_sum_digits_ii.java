// CONFIG class=Solution method=countValidSubarrays types=None
// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public long countValidSubarrays(int[] nums, int x) {
        List<Long>[] byRemainder = new ArrayList[10];
        for (int i = 0; i < 10; i++) byRemainder[i] = new ArrayList<>();
        byRemainder[0].add(0L);
        long prefix = 0, answer = 0;
        for (int value : nums) {
            prefix += value;
            int required = (int) ((prefix - x) % 10 + 10) % 10;
            List<Long> values = byRemainder[required];
            for (long power = 1; (long) x * power <= prefix; power *= 10) {
                long low = (long) x * power;
                long high = (long) (x + 1) * power - 1;
                long minPrefix = prefix - high, maxPrefix = prefix - low;
                int left = lowerBound(values, minPrefix);
                int right = upperBound(values, maxPrefix);
                answer += right - left;
                if (power > prefix / 10) break;
            }
            byRemainder[(int) (prefix % 10)].add(prefix);
        }
        return answer;
    }

    private int lowerBound(List<Long> a, long x) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a.get(mid) < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private int upperBound(List<Long> a, long x) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a.get(mid) <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
