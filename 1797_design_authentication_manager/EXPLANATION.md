# 1797. Design Authentication Manager

Hash map tokenId -> expiry; renew only if still unexpired, count by comparing to currentTime.
