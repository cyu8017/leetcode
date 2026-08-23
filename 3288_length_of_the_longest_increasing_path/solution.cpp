// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

#include <algorithm>
#include <vector>

class Solution {
    int lis(const std::vector<int>& a) {
        std::vector<int> tails;
        for (int x : a) {
            auto it = std::lower_bound(tails.begin(), tails.end(), x);
            if (it == tails.end()) tails.push_back(x);
            else *it = x;
        }
        return (int)tails.size();
    }

public:
    int maxPathLength(std::vector<std::vector<int>>& coordinates, int k) {
        int n = (int)coordinates.size();
        struct Pt { int x, y, i; };
        std::vector<Pt> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {coordinates[i][0], coordinates[i][1], i};
        std::sort(arr.begin(), arr.end(), [](const Pt& a, const Pt& b) {
            if (a.x == b.x) return a.y > b.y;
            return a.x < b.x;
        });
        int kx = coordinates[k][0], ky = coordinates[k][1];
        std::vector<int> left, right;
        for (auto& p : arr) {
            if (p.x < kx && p.y < ky) left.push_back(p.y);
            if (p.x > kx && p.y > ky) right.push_back(p.y);
        }
        return lis(left) + 1 + lis(right);
    }
};
