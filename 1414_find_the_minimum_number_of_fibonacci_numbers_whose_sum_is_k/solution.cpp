#include <vector>

class Solution {
public:
    int findMinFibonacciNumbers(int k) {
        std::vector<int> fib{1, 1};
        while (fib.back() < k) fib.push_back(fib.back() + fib[fib.size() - 2]);
        int answer = 0;
        for (int i = (int)fib.size() - 1; i >= 0; --i) {
            if (fib[i] <= k) { k -= fib[i]; ++answer; }
        }
        return answer;
    }
};
