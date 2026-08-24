# LeetCode 2129 - Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

# @param {String} title
# @return {String}
def capitalize_title(title)
  title.strip.split.map do |w|
    w = w.downcase
    w.length > 2 ? w[0].upcase + w[1..] : w
  end.join(" ")
end
