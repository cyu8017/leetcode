// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager(_timeToLive: Int) {
  private val ttl = _timeToLive
  private val tokens = scala.collection.mutable.Map.empty[String, Int]

  def generate(tokenId: String, currentTime: Int): Unit = {
    tokens(tokenId) = currentTime + ttl
  }

  def renew(tokenId: String, currentTime: Int): Unit = {
    tokens.get(tokenId) match {
      case Some(exp) if exp > currentTime => tokens(tokenId) = currentTime + ttl
      case _ =>
    }
  }

  def countUnexpiredTokens(currentTime: Int): Int = {
    tokens.values.count(_ > currentTime)
  }
}
