# LeetCode 0831 - Masking Personal Information
# https://leetcode.com/problems/masking-personal-information/

# @param {String} s
# @return {String}
def mask_pii(s)
  if s.include?("@")
    name, domain = s.downcase.split("@")
    return "#{name[0]}*****#{name[-1]}@#{domain}"
  end
  digits = s.chars.select { |ch| ch.match?(/\d/) }
  local = digits[-4..].join
  country = digits.length - 10
  return "***-***-#{local}" if country == 0

  "+" + ("*" * country) + "-***-***-#{local}"
end
