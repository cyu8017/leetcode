// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

object Solution {
  def validIPAddress(queryIP: String): String = {
    if (isIpv4(queryIP)) {
      "IPv4"
    } else if (isIpv6(queryIP)) {
      "IPv6"
    } else {
      "Neither"
    }
  }

  private def isIpv4(address: String): Boolean = {
    val parts = address.split("\\.", -1)
    if (parts.length != 4) {
      return false
    }

    parts.forall { part =>
      part.nonEmpty &&
      part.length <= 3 &&
      part.forall(_.isDigit) &&
      !(part.length > 1 && part.charAt(0) == '0') &&
      part.toInt <= 255
    }
  }

  private def isIpv6(address: String): Boolean = {
    val parts = address.split(":", -1)
    if (parts.length != 8) {
      return false
    }

    val hexDigits = "0123456789abcdefABCDEF"
    parts.forall { part =>
      part.nonEmpty &&
      part.length <= 4 &&
      part.forall(char => hexDigits.indexOf(char) >= 0)
    }
  }
}
