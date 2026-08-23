// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

#include <string>
#include <unordered_map>

class Codec {
    std::unordered_map<std::string, std::string> urlToCode_;
    std::unordered_map<std::string, std::string> codeToUrl_;
    int counter_ = 0;
    const std::string base_ = "http://tinyurl.com/";

public:
    std::string encode(std::string longUrl) {
        const auto existing = urlToCode_.find(longUrl);
        if (existing != urlToCode_.end()) {
            return existing->second;
        }
        const std::string code = std::to_string(counter_++);
        const std::string shortUrl = base_ + code;
        urlToCode_[longUrl] = shortUrl;
        codeToUrl_[shortUrl] = longUrl;
        return shortUrl;
    }

    std::string decode(std::string shortUrl) {
        return codeToUrl_.at(shortUrl);
    }
};
