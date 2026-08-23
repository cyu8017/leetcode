// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

#include <string>
#include <vector>
#include <unordered_map>

class Encrypter {
    std::unordered_map<char, std::string> enc;
    std::unordered_map<std::string, int> cnt;
public:
    Encrypter(std::vector<char>& keys, std::vector<std::string>& values, std::vector<std::string>& dictionary) {
        for (size_t i = 0; i < keys.size(); ++i) enc[keys[i]] = values[i];
        for (auto& w : dictionary) cnt[encrypt(w)]++;
    }

    std::string encrypt(std::string word1) {
        std::string b;
        b.reserve(word1.size() * 2);
        for (char c : word1) {
            auto it = enc.find(c);
            if (it == enc.end()) return "";
            b += it->second;
        }
        return b;
    }

    int decrypt(std::string word2) {
        return cnt[word2];
    }
};
