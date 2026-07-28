// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution {
    public double[] sampleStats(int[] count) {
        int total = 0;
        for (int c : count) {
            total += c;
        }
        int minimum = 0;
        for (int i = 0; i < 256; i++) {
            if (count[i] > 0) {
                minimum = i;
                break;
            }
        }
        int maximum = 0;
        for (int i = 255; i >= 0; i--) {
            if (count[i] > 0) {
                maximum = i;
                break;
            }
        }
        long sum = 0;
        for (int i = 0; i < 256; i++) {
            sum += (long) i * count[i];
        }
        double mean = (double) sum / total;
        int mode = 0;
        for (int i = 1; i < 256; i++) {
            if (count[i] > count[mode]) {
                mode = i;
            }
        }
        int mid1 = (total + 1) / 2;
        int mid2 = (total + 2) / 2;
        int seen = 0;
        int first = -1, second = -1;
        for (int i = 0; i < 256; i++) {
            seen += count[i];
            if (first < 0 && seen >= mid1) {
                first = i;
            }
            if (second < 0 && seen >= mid2) {
                second = i;
                break;
            }
        }
        double median = (first + second) / 2.0;
        return new double[] { minimum, maximum, mean, median, mode };
    }
}
