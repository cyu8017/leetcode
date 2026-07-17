// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

import java.util.HashMap;
import java.util.Map;

class AuthenticationManager {
    private final int ttl;
    private final Map<String, Integer> tokens = new HashMap<>();

    public AuthenticationManager(int timeToLive) {
        this.ttl = timeToLive;
    }

    public void generate(String tokenId, int currentTime) {
        tokens.put(tokenId, currentTime + ttl);
    }

    public void renew(String tokenId, int currentTime) {
        Integer exp = tokens.get(tokenId);
        if (exp != null && exp > currentTime) {
            tokens.put(tokenId, currentTime + ttl);
        }
    }

    public int countUnexpiredTokens(int currentTime) {
        int count = 0;
        for (int exp : tokens.values()) {
            if (exp > currentTime) count++;
        }
        return count;
    }
}
