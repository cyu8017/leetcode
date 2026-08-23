// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

#include <string>
#include <vector>

class Solution {
public:
    std::string getPermutation(int n, int k) {
        std::vector<int> numbers;
        std::vector<int> factorials(n, 1);

        for (int i = 0; i < n; ++i) {
            numbers.push_back(i + 1);
            if (i > 0) {
                factorials[i] = factorials[i - 1] * i;
            }
        }

        --k;
        std::string result;

        for (int i = n - 1; i >= 0; --i) {
            int index = k / factorials[i];
            result.push_back(static_cast<char>('0' + numbers[index]));
            numbers.erase(numbers.begin() + index);
            k %= factorials[i];
        }

        return result;
    }
};
