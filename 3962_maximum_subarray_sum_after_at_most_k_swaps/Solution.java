// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

import java.util.Arrays;

class Solution {
    private int[] unique;

    public long maxSubarraySum(int[] nums, int k) {
        int n = nums.length;
        unique = nums.clone();
        Arrays.sort(unique);
        int u = 0;
        for (int i = 0; i < unique.length; i++) {
            if (u == 0 || unique[i] != unique[u - 1]) unique[u++] = unique[i];
        }
        unique = Arrays.copyOf(unique, u);
        int[] rank = new int[n];
        int[] globalCount = new int[unique.length + 1];
        long[] globalSum = new long[unique.length + 1];
        for (int i = 0; i < n; i++) {
            rank[i] = lowerBound(unique, nums[i]) + 1;
            add(globalCount, globalSum, rank[i], 1);
        }
        long answer = -(1L << 60);
        for (int left = 0; left < n; left++) {
            int[] insideCount = new int[unique.length + 1];
            long[] insideSum = new long[unique.length + 1];
            int[] outsideCount = globalCount.clone();
            long[] outsideSum = globalSum.clone();
            long subarraySum = 0;
            for (int right = left; right < n; right++) {
                add(outsideCount, outsideSum, rank[right], -1);
                add(insideCount, insideSum, rank[right], 1);
                subarraySum += nums[right];
                int insideSize = right - left + 1;
                int outsideSize = n - insideSize;
                int limit = Math.min(k, Math.min(insideSize, outsideSize));
                int low = 0, high = limit;
                while (low < high) {
                    int mid = (low + high + 1) / 2;
                    int insideValue = unique[kth(insideCount, mid) - 1];
                    int outsideOrder = outsideSize - mid + 1;
                    int outsideValue = unique[kth(outsideCount, outsideOrder) - 1];
                    if (outsideValue > insideValue) low = mid;
                    else high = mid - 1;
                }
                int swaps = low;
                long gain = 0;
                if (swaps > 0) {
                    long smallInside = sumSmallest(insideCount, insideSum, swaps);
                    long totalOutside = querySum(outsideSum, unique.length);
                    long largeOutside = totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize - swaps);
                    gain = largeOutside - smallInside;
                }
                answer = Math.max(answer, subarraySum + gain);
            }
        }
        return answer;
    }

    private void add(int[] count, long[] sum, int index, int delta) {
        long value = unique[index - 1];
        for (; index < count.length; index += index & -index) {
            count[index] += delta;
            sum[index] += (long) delta * value;
        }
    }

    private int queryCount(int[] bit, int index) {
        int result = 0;
        for (; index > 0; index -= index & -index) result += bit[index];
        return result;
    }

    private long querySum(long[] bit, int index) {
        long result = 0;
        for (; index > 0; index -= index & -index) result += bit[index];
        return result;
    }

    private int kth(int[] bit, int order) {
        int index = 0, step = 1;
        while ((step << 1) < bit.length) step <<= 1;
        for (; step > 0; step >>= 1) {
            int next = index + step;
            if (next < bit.length && bit[next] < order) {
                index = next;
                order -= bit[next];
            }
        }
        return index + 1;
    }

    private long sumSmallest(int[] count, long[] sum, int amount) {
        if (amount <= 0) return 0;
        int index = kth(count, amount);
        int countBefore = queryCount(count, index - 1);
        long sumBefore = querySum(sum, index - 1);
        return sumBefore + (long) (amount - countBefore) * unique[index - 1];
    }

    private int lowerBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
