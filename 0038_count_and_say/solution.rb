# LeetCode 0038 - Count and Say
# https://leetcode.com/problems/count-and-say/

# @param {Integer} n
# @return {String}
def count_and_say(n)
  term = "1"

  (1...n).each do
    next_term = []
    index = 0
    while index < term.length
      count = 1
      while index + count < term.length && term[index + count] == term[index]
        count += 1
      end
      next_term << count.to_s
      next_term << term[index]
      index += count
    end
    term = next_term.join
  end

  term
end
