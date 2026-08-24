# LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

# @param {String} s
# @return {Integer}
def minimum_chairs(s)
  cnt = 0
  left = 0
  s.each_char do |c|
    if c == "E"
      if left > 0
        left -= 1
      else
        cnt += 1
      end
    else
      left += 1
    end
  end
  cnt
end
