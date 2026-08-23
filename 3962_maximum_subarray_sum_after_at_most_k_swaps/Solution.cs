// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxSubarraySum(int[] nums, int k) {
        int n = nums.Length;
        var unique = new List<int>(nums);
        unique.Sort();
        int w = 0;
        for (int i = 0; i < unique.Count; i++) {
            if (i == 0 || unique[i] != unique[i - 1]) unique[w++] = unique[i];
        }
        unique.RemoveRange(w, unique.Count - w);
        int[] rank = new int[n];
        int[] globalCount = new int[unique.Count + 1];
        long[] globalSum = new long[unique.Count + 1];
        void Add(int[] count, long[] sum, int index, int delta) {
            long value = unique[index - 1];
            for (; index < count.Length; index += index & -index) {
                count[index] += delta;
                sum[index] += (long)delta * value;
            }
        }
        int LowerBound(int x) {
            int lo = 0, hi = unique.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (unique[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }
        for (int i = 0; i < n; i++) {
            rank[i] = LowerBound(nums[i]) + 1;
            Add(globalCount, globalSum, rank[i], 1);
        }
        int QueryCount(int[] bit, int index) {
            int result = 0;
            for (; index > 0; index -= index & -index) result += bit[index];
            return result;
        }
        long QuerySum(long[] bit, int index) {
            long result = 0;
            for (; index > 0; index -= index & -index) result += bit[index];
            return result;
        }
        int Kth(int[] bit, int order) {
            int index = 0, step = 1;
            while ((step << 1) < bit.Length) step <<= 1;
            for (; step > 0; step >>= 1) {
                int next = index + step;
                if (next < bit.Length && bit[next] < order) {
                    index = next;
                    order -= bit[next];
                }
            }
            return index + 1;
        }
        long SumSmallest(int[] count, long[] sum, int amount) {
            if (amount <= 0) return 0;
            int index = Kth(count, amount);
            int countBefore = QueryCount(count, index - 1);
            long sumBefore = QuerySum(sum, index - 1);
            return sumBefore + (long)(amount - countBefore) * unique[index - 1];
        }
        long answer = -(1L << 60);
        for (int left = 0; left < n; left++) {
            int[] insideCount = new int[unique.Count + 1];
            long[] insideSum = new long[unique.Count + 1];
            int[] outsideCount = (int[])globalCount.Clone();
            long[] outsideSum = (long[])globalSum.Clone();
            long subarraySum = 0;
            for (int right = left; right < n; right++) {
                Add(outsideCount, outsideSum, rank[right], -1);
                Add(insideCount, insideSum, rank[right], 1);
                subarraySum += nums[right];
                int insideSize = right - left + 1;
                int outsideSize = n - insideSize;
                int limit = Math.Min(k, Math.Min(insideSize, outsideSize));
                int low = 0, high = limit;
                while (low < high) {
                    int mid = (low + high + 1) / 2;
                    int insideValue = unique[Kth(insideCount, mid) - 1];
                    int outsideOrder = outsideSize - mid + 1;
                    int outsideValue = unique[Kth(outsideCount, outsideOrder) - 1];
                    if (outsideValue > insideValue) low = mid;
                    else high = mid - 1;
                }
                int swaps = low;
                long gain = 0;
                if (swaps > 0) {
                    long smallInside = SumSmallest(insideCount, insideSum, swaps);
                    long totalOutside = QuerySum(outsideSum, unique.Count);
                    long largeOutside = totalOutside - SumSmallest(outsideCount, outsideSum, outsideSize - swaps);
                    gain = largeOutside - smallInside;
                }
                answer = Math.Max(answer, subarraySum + gain);
            }
        }
        return answer;
    }
}
