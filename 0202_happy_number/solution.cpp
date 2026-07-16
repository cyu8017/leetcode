// LeetCode 0202 - Happy Number
#include <unordered_set>

class Solution {
public:
    bool isHappy(int n) {
        std::unordered_set<int> seen;
        while (n != 1 && !seen.count(n)) { seen.insert(n); n = nextValue(n); }
        return n == 1;
    }
private:
    int nextValue(int n) { int total = 0; while (n) { int digit = n % 10; total += digit * digit; n /= 10; } return total; }
};
