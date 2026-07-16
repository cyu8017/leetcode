class AuthenticationManager:
    def __init__(self, timeToLive):
        self.ttl = timeToLive
        self.tokens = {}
    def generate(self, tokenId, currentTime):
        self.tokens[tokenId] = currentTime + self.ttl
    def renew(self, tokenId, currentTime):
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl
    def countUnexpiredTokens(self, currentTime):
        return sum(exp > currentTime for exp in self.tokens.values())
