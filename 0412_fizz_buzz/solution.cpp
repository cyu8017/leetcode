// LeetCode 0412 - Fizz Buzz
// https://leetcode.com/problems/fizz-buzz/

#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> result;
        result.reserve(n);

        for (int value = 1; value <= n; ++value) {
            if (value % 15 == 0) {
                result.push_back("FizzBuzz");
            } else if (value % 3 == 0) {
                result.push_back("Fizz");
            } else if (value % 5 == 0) {
                result.push_back("Buzz");
            } else {
                result.push_back(to_string(value));
            }
        }

        return result;
    }
};
