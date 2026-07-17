"use strict";
// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthenticationManager = void 0;
class AuthenticationManager {
    constructor(timeToLive) {
        this.tokens = new Map();
        this.ttl = timeToLive;
    }
    generate(tokenId, currentTime) {
        this.tokens.set(tokenId, currentTime + this.ttl);
        return null;
    }
    renew(tokenId, currentTime) {
        const exp = this.tokens.get(tokenId);
        if (exp !== undefined && exp > currentTime) {
            this.tokens.set(tokenId, currentTime + this.ttl);
        }
        return null;
    }
    countUnexpiredTokens(currentTime) {
        let count = 0;
        for (const exp of this.tokens.values()) {
            if (exp > currentTime)
                count++;
        }
        return count;
    }
}
exports.AuthenticationManager = AuthenticationManager;
