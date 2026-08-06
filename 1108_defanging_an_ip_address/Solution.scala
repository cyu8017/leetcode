// LeetCode 1108 - Defanging an IP Address
// https://leetcode.com/problems/defanging-an-ip-address/

object Solution {
  def defangIPaddr(address: String): String = {
    address.replace(".", "[.]")
  }
}
