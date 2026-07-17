// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

import java.util.Arrays;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int minWastedSpace(int[] packages, int[][] boxes) {
        Arrays.sort(packages);
        long[] prefix = new long[packages.length];
        long total = 0;
        for (int i = 0; i < packages.length; i++) {
            total += packages[i];
            prefix[i] = total;
        }

        long answer = Long.MAX_VALUE;
        for (int[] supplier : boxes) {
            Arrays.sort(supplier);
            int start = 0;
            long wasted = 0;
            for (int box : supplier) {
                int end = upperBound(packages, box, start, packages.length);
                if (end == start) {
                    continue;
                }
                long packageSum = prefix[end - 1] - (start > 0 ? prefix[start - 1] : 0);
                wasted += (long) box * (end - start) - packageSum;
                start = end;
            }
            if (start == packages.length) {
                answer = Math.min(answer, wasted);
            }
        }

        return answer == Long.MAX_VALUE ? -1 : (int) (answer % MOD);
    }

    private int upperBound(int[] values, int target, int lo, int hi) {
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (values[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
