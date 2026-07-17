// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

public class AuthenticationManager {
    private readonly int ttl;
    private readonly Dictionary<string, int> tokens = new Dictionary<string, int>();

    public AuthenticationManager(int timeToLive) {
        ttl = timeToLive;
    }

    public void Generate(string tokenId, int currentTime) {
        tokens[tokenId] = currentTime + ttl;
    }

    public void Renew(string tokenId, int currentTime) {
        if (tokens.TryGetValue(tokenId, out int exp) && exp > currentTime) {
            tokens[tokenId] = currentTime + ttl;
        }
    }

    public int CountUnexpiredTokens(int currentTime) {
        int count = 0;
        foreach (int exp in tokens.Values) {
            if (exp > currentTime) count++;
        }
        return count;
    }
}
