// LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

#include <string>
#include <unordered_map>

class Solution {
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    int atLeast(const std::string& word, int k) {
        std::unordered_map<char, int> cnt;
        int cons = 0, l = 0, ans = 0;
        for (int r = 0; r < (int)word.size(); r++) {
            char c = word[r];
            if (isVowel(c)) cnt[c]++;
            else cons++;
            while ((int)cnt.size() == 5 && cons >= k) {
                ans += (int)word.size() - r;
                char c2 = word[l];
                if (isVowel(c2)) {
                    if (--cnt[c2] == 0) cnt.erase(c2);
                } else cons--;
                l++;
            }
        }
        return ans;
    }

public:
    int countOfSubstrings(std::string word, int k) {
        return atLeast(word, k) - atLeast(word, k + 1);
    }
};
