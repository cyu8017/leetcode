// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager {
    private let ttl: Int
    private var tokens: [String: Int] = [:]

    init(_ timeToLive: Int) {
        self.ttl = timeToLive
    }

    func generate(_ tokenId: String, _ currentTime: Int) {
        tokens[tokenId] = currentTime + ttl
    }

    func renew(_ tokenId: String, _ currentTime: Int) {
        if let exp = tokens[tokenId], exp > currentTime {
            tokens[tokenId] = currentTime + ttl
        }
    }

    func countUnexpiredTokens(_ currentTime: Int) -> Int {
        return tokens.values.filter { $0 > currentTime }.count
    }
}
