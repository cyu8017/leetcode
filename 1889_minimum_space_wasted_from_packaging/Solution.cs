// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

public class Solution {
    public int MinWastedSpace(int[] packages, int[][] boxes) {
        Array.Sort(packages);
        var prefix = new long[packages.Length];
        prefix[0] = packages[0];
        for (int i = 1; i < packages.Length; i++) {
            prefix[i] = prefix[i - 1] + packages[i];
        }

        long answer = long.MaxValue;
        foreach (int[] supplier in boxes) {
            var sortedBoxes = (int[])supplier.Clone();
            Array.Sort(sortedBoxes);
            int start = 0;
            long wasted = 0;
            bool ok = true;
            foreach (int box in sortedBoxes) {
                if (!ok) {
                    break;
                }
                int lo = start;
                int hi = packages.Length;
                while (lo < hi) {
                    int mid = lo + (hi - lo) / 2;
                    if (packages[mid] <= box) {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }
                int end = lo;
                if (end != start) {
                    long packageSum = prefix[end - 1] - (start > 0 ? prefix[start - 1] : 0L);
                    wasted += (long)box * (end - start) - packageSum;
                    start = end;
                }
            }
            if (start == packages.Length) {
                answer = Math.Min(answer, wasted);
            }
        }
        return answer == long.MaxValue ? -1 : (int)(answer % 1_000_000_007L);
    }
}
