// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager(private val timeToLive: Int) {
    private val tokens = HashMap<String, Int>()

    fun generate(tokenId: String, currentTime: Int) {
        tokens[tokenId] = currentTime + timeToLive
    }

    fun renew(tokenId: String, currentTime: Int) {
        val exp = tokens[tokenId]
        if (exp != null && exp > currentTime) {
            tokens[tokenId] = currentTime + timeToLive
        }
    }

    fun countUnexpiredTokens(currentTime: Int): Int {
        return tokens.values.count { it > currentTime }
    }
}
