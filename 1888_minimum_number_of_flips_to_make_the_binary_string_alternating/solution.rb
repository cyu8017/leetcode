# LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

# @param {String} s
# @return {Integer}
def min_flips(s)
  n = s.length
  doubled = s + s
  alt0 = alt1 = 0

  (0...n).each do |i|
    alt0 += 1 if doubled[i] != (i.even? ? "0" : "1")
    alt1 += 1 if doubled[i] != (i.even? ? "1" : "0")
  end

  answer = [alt0, alt1].min
  (0...n).each do |i|
    alt0 -= 1 if doubled[i] != (i.even? ? "0" : "1")
    alt0 += 1 if doubled[i + n] != ((i + n).even? ? "0" : "1")

    alt1 -= 1 if doubled[i] != (i.even? ? "1" : "0")
    alt1 += 1 if doubled[i + n] != ((i + n).even? ? "1" : "0")

    answer = [answer, alt0, alt1].min
  end

  answer
end
