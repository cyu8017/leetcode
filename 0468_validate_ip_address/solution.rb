# LeetCode 0468 - Validate IP Address
# https://leetcode.com/problems/validate-ip-address/

class Solution
  def valid_ip_address(query_ip)
    return "IPv4" if ipv4?(query_ip)
    return "IPv6" if ipv6?(query_ip)

    "Neither"
  end

  alias_method :validIPAddress, :valid_ip_address

  private

  def ipv4?(address)
    parts = address.split(".")
    return false unless parts.length == 4

    parts.all? do |part|
      next false unless part.match?(/\A\d+\z/)
      next false if part.length > 1 && part[0] == "0"
      next false if part.empty? || part.length > 3

      value = part.to_i
      value <= 255
    end
  end

  def ipv6?(address)
    parts = address.split(":")
    return false unless parts.length == 8

    hex_digits = "0123456789abcdefABCDEF"
    parts.all? do |part|
      !part.empty? && part.length <= 4 && part.chars.all? { |char| hex_digits.include?(char) }
    end
  end
end
