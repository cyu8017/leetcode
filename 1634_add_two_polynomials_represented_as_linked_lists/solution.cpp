// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> addPoly(std::vector<std::vector<int>>& poly1,
                                          std::vector<std::vector<int>>& poly2) {
        std::vector<std::vector<int>> out;
        size_t i = 0, j = 0;
        while (i < poly1.size() || j < poly2.size()) {
            int c, p;
            if (j == poly2.size() || (i < poly1.size() && poly1[i][1] > poly2[j][1])) {
                c = poly1[i][0];
                p = poly1[i][1];
                ++i;
            } else if (i == poly1.size() || poly2[j][1] > poly1[i][1]) {
                c = poly2[j][0];
                p = poly2[j][1];
                ++j;
            } else {
                c = poly1[i][0] + poly2[j][0];
                p = poly1[i][1];
                ++i;
                ++j;
            }
            if (c) {
                out.push_back({c, p});
            }
        }
        return out;
    }
};
