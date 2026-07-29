// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

#include <set>
#include <vector>

class Solution {
public:
    std::vector<int> arraysIntersection(std::vector<int>& arr1, std::vector<int>& arr2, std::vector<int>& arr3) {
        std::set<int> s1(arr1.begin(), arr1.end());
        std::set<int> s2(arr2.begin(), arr2.end());
        std::set<int> s3(arr3.begin(), arr3.end());
        std::vector<int> answer;
        for (int x : s1) {
            if (s2.count(x) && s3.count(x)) {
                answer.push_back(x);
            }
        }
        return answer;
    }
};
