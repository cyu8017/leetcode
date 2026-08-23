// LeetCode 0418 - Sentence Screen Fitting
// https://leetcode.com/problems/sentence-screen-fitting/

#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int wordsTyping(vector<string>& sentence, int rows, int cols) {
        int count = 0;
        int index = 0;
        int total = (int)sentence.size();

        for (int row = 0; row < rows; ++row) {
            int col = 0;
            while (true) {
                const string& word = sentence[index];
                int needed = (int)word.size() + (col > 0 ? 1 : 0);
                if (col + needed > cols) {
                    break;
                }
                if (col > 0) {
                    ++col;
                }
                col += (int)word.size();
                index = (index + 1) % total;
                if (index == 0) {
                    ++count;
                }
            }
        }

        return count;
    }
};
