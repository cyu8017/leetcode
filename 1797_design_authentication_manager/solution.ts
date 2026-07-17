// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

export class AuthenticationManager {
    private readonly ttl: number;
    private readonly tokens = new Map<string, number>();

    constructor(timeToLive: number) {
        this.ttl = timeToLive;
    }

    generate(tokenId: string, currentTime: number): null {
        this.tokens.set(tokenId, currentTime + this.ttl);
        return null;
    }

    renew(tokenId: string, currentTime: number): null {
        const exp = this.tokens.get(tokenId);
        if (exp !== undefined && exp > currentTime) {
            this.tokens.set(tokenId, currentTime + this.ttl);
        }
        return null;
    }

    countUnexpiredTokens(currentTime: number): number {
        let count = 0;
        for (const exp of this.tokens.values()) {
            if (exp > currentTime) count++;
        }
        return count;
    }
}
