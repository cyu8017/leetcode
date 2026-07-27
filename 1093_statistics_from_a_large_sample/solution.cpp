// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

#include <vector>

class Solution {
public:
    std::vector<double> sampleStats(std::vector<int>& count) {
        long long total = 0;
        for (int c : count) {
            total += c;
        }
        int minimum = 0;
        while (minimum < 256 && count[minimum] == 0) {
            ++minimum;
        }
        int maximum = 255;
        while (maximum >= 0 && count[maximum] == 0) {
            --maximum;
        }
        long long sum = 0;
        int mode = 0;
        for (int i = 0; i < 256; ++i) {
            sum += 1LL * i * count[i];
            if (count[i] > count[mode]) {
                mode = i;
            }
        }
        double mean = static_cast<double>(sum) / static_cast<double>(total);
        long long mid1 = (total + 1) / 2;
        long long mid2 = (total + 2) / 2;
        long long seen = 0;
        int first = -1;
        int second = -1;
        for (int i = 0; i < 256; ++i) {
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
        return {static_cast<double>(minimum), static_cast<double>(maximum), mean, median,
                static_cast<double>(mode)};
    }
};
