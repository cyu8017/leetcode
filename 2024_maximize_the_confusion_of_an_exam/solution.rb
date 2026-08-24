# LeetCode 2024 - Maximize the Confusion of an Exam
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

# @param {String} answer_key
# @param {Integer} k
# @return {Integer}
def max_consecutive_answers(answer_key, k)
  max_with = lambda do |ch|
    left = bad = best = 0
    answer_key.each_char.with_index do |c, right|
      bad += 1 if c != ch
      while bad > k
        bad -= 1 if answer_key[left] != ch
        left += 1
      end
      best = [best, right - left + 1].max
    end
    best
  end
  [max_with.call("T"), max_with.call("F")].max
end
