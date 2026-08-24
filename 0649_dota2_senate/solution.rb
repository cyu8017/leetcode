# LeetCode 0649 - Dota2 Senate
# https://leetcode.com/problems/dota2-senate/

# @param {String} senate
# @return {String}
def predict_party_victory(senate)
  radiant = []
  dire = []
  n = senate.length

  senate.each_char.with_index do |senator, i|
    if senator == "R"
      radiant << i
    else
      dire << i
    end
  end

  until radiant.empty? || dire.empty?
    r = radiant.shift
    d = dire.shift
    if r < d
      radiant << r + n
    else
      dire << d + n
    end
  end

  radiant.empty? ? "Dire" : "Radiant"
end
