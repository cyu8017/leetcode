// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

#include <string>
#include <vector>

class Solution {
    static void buildLPS(std::vector<int>& lps, const std::string& pattern) {
        int l = 0, i = 1, s_l = (int)pattern.size();
        lps[0] = 0;
        while (i < s_l) {
            if (pattern[i] == pattern[l]) {
                l++;
                lps[i] = l;
                i++;
            } else if (l != 0) {
                l = lps[l - 1];
            } else {
                lps[i] = l;
                i++;
            }
        }
    }
    static void kmp(const std::string& s, const std::string& pat, const std::vector<int>& lps, std::vector<int>& index) {
        int s_len = (int)s.size(), pat_l = (int)pat.size();
        int i = 0, j = 0;
        while (s_len - i >= pat_l - j) {
            if (s[i] == pat[j]) {
                i++;
                j++;
            }
            if (j == pat_l) {
                index.push_back(i - pat_l);
                j = lps[j - 1];
            } else if (i < s_len && s[i] != pat[j]) {
                if (j != 0) j = lps[j - 1];
                else i++;
            }
        }
    }
public:
    std::vector<int> beautifulIndices(std::string s, std::string a, std::string b, int k) {
        int a_len = (int)a.size(), b_len = (int)b.size();
        std::vector<int> lps_a(a_len), lps_b(b_len), a_index, b_index, final;
        buildLPS(lps_a, a);
        buildLPS(lps_b, b);
        kmp(s, a, lps_a, a_index);
        kmp(s, b, lps_b, b_index);
        int i = 0, j = 0;
        while (i < (int)a_index.size() && j < (int)b_index.size()) {
            if (a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j]) {
                final.push_back(a_index[i]);
                i++;
            } else if (a_index[i] - k > b_index[j]) {
                j++;
            } else {
                i++;
            }
        }
        return final;
    }
};
