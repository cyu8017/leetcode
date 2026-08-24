# LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

# @param {String} s
# @return {String}
def find_latest_time(s)
  h = 11
  loop do
    59.downto(0) do |m|
      t = format("%02d:%02d", h, m)
      ok = true
      5.times do |i|
        if s[i] != "?" && s[i] != t[i]
          ok = false
          break
        end
      end
      return t if ok
    end
    h -= 1
  end
end
