// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager {
    /**
     * @param {number} timeToLive
     */
    constructor(timeToLive) {
        this.ttl = timeToLive;
        this.tokens = new Map();
    }

    /**
     * @param {string} tokenId
     * @param {number} currentTime
     * @return {null}
     */
    generate(tokenId, currentTime) {
        this.tokens.set(tokenId, currentTime + this.ttl);
        return null;
    }

    /**
     * @param {string} tokenId
     * @param {number} currentTime
     * @return {null}
     */
    renew(tokenId, currentTime) {
        if (this.tokens.has(tokenId) && this.tokens.get(tokenId) > currentTime) {
            this.tokens.set(tokenId, currentTime + this.ttl);
        }
        return null;
    }

    /**
     * @param {number} currentTime
     * @return {number}
     */
    countUnexpiredTokens(currentTime) {
        let count = 0;
        for (const exp of this.tokens.values()) {
            if (exp > currentTime) count++;
        }
        return count;
    }
}

module.exports = { AuthenticationManager };
