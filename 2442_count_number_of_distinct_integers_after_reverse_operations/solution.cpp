// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int countDistinctIntegers(std::vector<int>& nums) {
        auto rev = [](int x) {
            int r = 0;
            while (x > 0) {
                r = r * 10 + x % 10;
                x /= 10;
            }
            return r;
        };
        std::unordered_set<int> seen;
        for (int x : nums) {
            seen.insert(x);
            seen.insert(rev(x));
        }
        return (int)seen.size();
    }
};
