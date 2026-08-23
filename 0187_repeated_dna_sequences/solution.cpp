// LeetCode 0187 - Repeated DNA Sequences
// https://leetcode.com/problems/repeated-dna-sequences/

#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_set<string> seen;
        unordered_set<string> repeated;
        for (int i = 0; i + 10 <= static_cast<int>(s.size()); ++i) {
            string sequence = s.substr(i, 10);
            if (!seen.insert(sequence).second) {
                repeated.insert(sequence);
            }
        }
        return {repeated.begin(), repeated.end()};
    }
};