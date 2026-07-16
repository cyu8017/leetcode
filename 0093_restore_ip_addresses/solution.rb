# LeetCode 0093 - Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses/

# @param {String} s
# @return {String[]}
def restore_ip_addresses(s)
  result = []
  path = []

  backtrack = lambda do |start|
    if path.length == 4
      result << path.join('.') if start == s.length
      return
    end

    (1..3).each do |length|
      break if start + length > s.length

      part = s[start, length]
      next if (part.start_with?('0') && part.length > 1) || part.to_i > 255

      path << part
      backtrack.call(start + length)
      path.pop
    end
  end

  backtrack.call(0)
  result
end
