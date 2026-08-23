// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

#include <algorithm>
#include <climits>
#include <cstdlib>
#include <set>
#include <vector>

class Solution {
public:
    int closestToTarget(std::vector<int>& arr, int target) {
        int answer = INT_MAX;
        std::set<int> current;
        for (int value : arr) {
            std::set<int> next;
            next.insert(value);
            for (int previous : current) {
                next.insert(value & previous);
            }
            current = std::move(next);
            for (int candidate : current) {
                answer = std::min(answer, std::abs(candidate - target));
            }
        }
        return answer;
    }
};
