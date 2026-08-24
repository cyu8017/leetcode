# LeetCode 0816 - Ambiguous Coordinates
# https://leetcode.com/problems/ambiguous-coordinates/

# @param {String} s
# @return {String[]}
def ambiguous_coordinates(s)
  digits = s[1...-1]

  candidates = lambda do |frag|
    options = []
    return options if frag.empty? || (frag.length > 1 && frag[0] == "0" && frag[-1] == "0")
    return frag[-1] != "0" ? ["0.#{frag[1..]}"] : [] if frag[0] == "0" && frag.length > 1

    unless frag[-1] == "0"
      (1...frag.length).each { |i| options << "#{frag[0...i]}.#{frag[i..]}" }
    end
    options << frag
    options
  end

  answer = []
  (1...digits.length).each do |i|
    candidates.call(digits[0...i]).each do |left|
      candidates.call(digits[i..]).each do |right|
        answer << "(#{left}, #{right})"
      end
    end
  end
  answer
end
