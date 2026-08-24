# LeetCode 0972 - Equal Rational Numbers
# https://leetcode.com/problems/equal-rational-numbers/

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_rational_equal(s, t)
  parse = lambda do |x|
    return Rational(x.empty? ? 0 : x) unless x.include?("(")

    non_rep, rest = x.split("(", 2)
    rep = rest[0...-1]
    non_rep += "." unless non_rep.include?(".")
    integer, frac = non_rep.split(".", 2)
    frac ||= ""
    base = Rational((integer.nil? || integer.empty?) ? 0 : integer.to_i)
    base += Rational(frac.to_i, 10**frac.length) unless frac.empty?
    base += Rational(rep.to_i, (10**rep.length - 1) * 10**frac.length) unless rep.empty?
    base
  end
  parse.call(s) == parse.call(t)
end
