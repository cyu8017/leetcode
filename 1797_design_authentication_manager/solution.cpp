// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

#include <string>
#include <unordered_map>

class AuthenticationManager {
public:
    AuthenticationManager(int timeToLive) : ttl(timeToLive) {}

    void generate(std::string tokenId, int currentTime) {
        tokens[tokenId] = currentTime + ttl;
    }

    void renew(std::string tokenId, int currentTime) {
        auto it = tokens.find(tokenId);
        if (it != tokens.end() && it->second > currentTime) {
            it->second = currentTime + ttl;
        }
    }

    int countUnexpiredTokens(int currentTime) {
        int count = 0;
        for (const auto& [tokenId, exp] : tokens) {
            if (exp > currentTime) count++;
        }
        return count;
    }

private:
    int ttl;
    std::unordered_map<std::string, int> tokens;
};
