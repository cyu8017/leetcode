# LeetCode 1304 - Find N Unique Integers Sum Up To Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

def sum_zero(n)
  answer = []
  (1..(n / 2)).each do |value|
    answer << -value << value
  end
  answer << 0 if n.odd?
  answer
end
