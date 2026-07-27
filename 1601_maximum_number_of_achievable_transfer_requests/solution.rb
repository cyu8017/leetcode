# LeetCode 1601 - Maximum Number of Achievable Transfer Requests
# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

# @param {Integer} n
# @param {Integer[][]} requests
# @return {Integer}
def maximum_requests(n, requests)
  ans = 0
  m = requests.length
  (0...(1 << m)).each do |mask|
    bits = mask.to_s(2).count("1")
    next if bits <= ans

    bal = Array.new(n, 0)
    requests.each_with_index do |(a, b), i|
      next if (mask >> i & 1).zero?

      bal[a] -= 1
      bal[b] += 1
    end
    ans = bits if bal.all?(&:zero?)
  end
  ans
end
