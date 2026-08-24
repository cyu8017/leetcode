# LeetCode 0751 - IP to CIDR
# https://leetcode.com/problems/ip-to-cidr/

# @param {String} ip
# @param {Integer} n
# @return {String[]}
def ip_to_cidr(ip, n)
  ip_to_int = lambda do |value|
    result = 0
    value.split(".").each { |part| result = result * 256 + part.to_i }
    result
  end

  int_to_ip = lambda do |value|
    [24, 16, 8, 0].map { |shift| ((value >> shift) & 255).to_s }.join(".")
  end

  start = ip_to_int.call(ip)
  answer = []
  while n > 0
    lowbit = start.zero? ? (1 << 32) : (start & -start)
    lowbit >>= 1 while lowbit > n
    mask = 32 - (lowbit.bit_length - 1)
    answer << "#{int_to_ip.call(start)}/#{mask}"
    start += lowbit
    n -= lowbit
  end
  answer
end
