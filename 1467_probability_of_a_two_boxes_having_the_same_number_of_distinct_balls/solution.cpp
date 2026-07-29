#include <vector>

class Solution {
    std::vector<int> balls;
    int half;
    long double good = 0, total = 0;
    long double comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        long double r = 1;
        for (int i = 1; i <= k; ++i) r = r * (n - k + i) / i;
        return r;
    }
    void dfs(int i, int left, int dl, long double ways) {
        if (i == (int)balls.size()) {
            if (left == half) {
                total += ways;
                if (dl == 0) good += ways;
            }
            return;
        }
        for (int x = 0; x <= balls[i]; ++x) {
            if (left + x <= half)
                dfs(i + 1, left + x, dl + (x > 0) - (x < balls[i]), ways * comb(balls[i], x));
        }
    }
public:
    double getProbability(std::vector<int>& balls_) {
        balls = balls_;
        half = 0;
        for (int b : balls) half += b;
        half /= 2;
        dfs(0, 0, 0, 1);
        return (double)(good / total);
    }
};
