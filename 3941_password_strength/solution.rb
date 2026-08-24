# LeetCode 3941 - Password Strength
# https://leetcode.com/problems/password-strength/

# @param {String} password
# @return {Integer}
def password_strength(password)
  ans = 0
  password.chars.uniq.each do |ch|
    if ch =~ /[a-z]/
      ans += 1
    elsif ch =~ /[A-Z]/
      ans += 2
    elsif ch =~ /[0-9]/
      ans += 3
    else
      ans += 5
    end
  end
  ans
end
