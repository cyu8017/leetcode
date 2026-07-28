// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

public class Solution {
    public double[] SampleStats(int[] count) {
        long total = 0;
        for (int i = 0; i < count.Length; i++) {
            total += count[i];
        }
        int minimum = 0;
        while (count[minimum] == 0) {
            minimum++;
        }
        int maximum = 255;
        while (count[maximum] == 0) {
            maximum--;
        }
        double mean = 0;
        for (int i = 0; i < 256; i++) {
            mean += (double)i * count[i];
        }
        mean /= total;
        int mode = 0;
        for (int i = 1; i < 256; i++) {
            if (count[i] > count[mode]) {
                mode = i;
            }
        }
        long mid1 = (total + 1) / 2;
        long mid2 = (total + 2) / 2;
        long seen = 0;
        int? first = null, second = null;
        for (int i = 0; i < 256; i++) {
            seen += count[i];
            if (first == null && seen >= mid1) {
                first = i;
            }
            if (second == null && seen >= mid2) {
                second = i;
                break;
            }
        }
        double median = (first.Value + second.Value) / 2.0;
        return new double[] { minimum, maximum, mean, median, mode };
    }
}
